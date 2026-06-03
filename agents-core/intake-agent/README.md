# Medivora Intake & Triage Agent

This is the Python backend for the Intake & Triage Agent. It uses FastAPI and Google's Gemini API (via Pydantic structured extraction) to parse raw medical text into structured E2B(R3) format.

## Setup Instructions

1. **Get an API Key**
   You need a free Google Gemini API key. Get one from [Google AI Studio](https://aistudio.google.com/).

2. **Configure Environment**
   Create a `.env` file in this folder and add your key:
   ```bash
   echo "GEMINI_API_KEY=your_actual_key_here" > .env
   ```

3. **Install Dependencies**
   (Assuming you are in the `agents-core/intake-agent` folder)
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

4. **Run the Server**
   ```bash
   uvicorn main:app --reload --port 8000
   ```

5. **Test the Demo**
   Make sure your Astro frontend is running (`npm run dev`).
   Go to `http://localhost:4321/demo/intake` and click "Run Extraction Agent".
