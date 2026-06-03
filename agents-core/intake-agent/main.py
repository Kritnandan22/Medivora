import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List, Optional
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API
API_KEY = os.getenv("GEMINI_API_KEY")
if API_KEY:
    genai.configure(api_key=API_KEY)

app = FastAPI(
    title="Medivora Intake & Triage Agent API",
    description="Automated extraction of E2B(R3) ICSR elements from unstructured source documents.",
    version="1.0.0"
)

# Enable CORS for the Astro frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, restrict this to the frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Pydantic Data Models (E2B Schema) ---

class PatientDetails(BaseModel):
    age: Optional[str] = Field(None, description="Age or date of birth of the patient")
    gender: Optional[str] = Field(None, description="Gender of the patient (e.g., Male, Female)")
    medical_history: Optional[str] = Field(None, description="Relevant past medical history")

class ReporterDetails(BaseModel):
    reporter_type: Optional[str] = Field(None, description="Qualification/Type of reporter (e.g., Physician, Consumer, Nurse)")
    country: Optional[str] = Field(None, description="Country of the reporter if mentioned")

class DrugDetails(BaseModel):
    drug_name: Optional[str] = Field(None, description="Name of the suspect drug")
    indication: Optional[str] = Field(None, description="Reason the drug was prescribed/taken")
    dosage: Optional[str] = Field(None, description="Dosage and frequency")

class AdverseEventDetails(BaseModel):
    event_term: Optional[str] = Field(None, description="The adverse event, reaction, or symptom experienced")
    onset_date: Optional[str] = Field(None, description="When the event started")
    outcome: Optional[str] = Field(None, description="Outcome of the event (e.g., Recovered, Fatal, Unknown)")

class ICSRExtraction(BaseModel):
    patient: Optional[PatientDetails] = Field(None, description="Details about the patient")
    reporter: Optional[ReporterDetails] = Field(None, description="Details about the reporter")
    suspect_drugs: List[DrugDetails] = Field(default_factory=list, description="List of all suspect drugs mentioned")
    adverse_events: List[AdverseEventDetails] = Field(default_factory=list, description="List of all adverse events mentioned")
    is_valid_case: bool = Field(..., description="True ONLY IF ALL 4 criteria are present: identifiable patient, identifiable reporter, suspect drug, and adverse event.")
    validation_reasoning: str = Field(..., description="Step-by-step reasoning explaining why the case is valid or invalid based on the 4 minimum criteria.")

# --- API Endpoints ---

class ExtractionRequest(BaseModel):
    source_text: str

@app.post("/api/extract", response_model=ICSRExtraction)
async def extract_icsr(request: ExtractionRequest):
    if not API_KEY:
        raise HTTPException(status_code=500, detail="GEMINI_API_KEY is not configured in the environment.")
    
    if not request.source_text.strip():
        raise HTTPException(status_code=400, detail="Source text cannot be empty.")
    
    try:
        # We use the gemini-1.5-pro-latest model for high accuracy complex extraction
        # Alternatively, gemini-1.5-flash can be used for speed
        model = genai.GenerativeModel('gemini-1.5-pro-latest')
        
        prompt = f"""
        You are an expert Pharmacovigilance Intake & Triage Agent.
        Your task is to extract Individual Case Safety Report (ICSR) elements from the following unstructured source text.
        
        You must strictly extract the 4 minimum criteria for a valid case:
        1. Identifiable Patient (age, gender, initials)
        2. Identifiable Reporter (physician, consumer, etc.)
        3. Suspect Drug
        4. Adverse Event
        
        If any of these 4 are completely missing, set 'is_valid_case' to false, but still extract whatever information is available.
        If all 4 are present, set 'is_valid_case' to true.
        Provide a brief explanation in 'validation_reasoning'.
        
        Source Text:
        \"\"\"{request.source_text}\"\"\"
        """
        
        # Call the Gemini API and force it to return the response matching our Pydantic schema
        result = model.generate_content(
            prompt,
            generation_config=genai.GenerationConfig(
                response_mime_type="application/json",
                response_schema=ICSRExtraction
            )
        )
        
        return result.text
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/health")
async def health_check():
    return {"status": "ok", "agent": "Intake & Triage", "llm_configured": bool(API_KEY)}
