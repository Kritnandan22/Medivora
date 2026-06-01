> Auto-converted from `Rx-Automata-Website-Build-Spec.docx` via pandoc.
> Source of truth for the build. If this contradicts `CLAUDE.md`, this wins.

# Rx Automata — Build Specification & Content Master

### BUILD SPECIFICATION · CONTENT MASTER

### Rx Automata

A production-grade website on agentic & workflow automation in pharmaceuticals and medicine management

Everything required to build, host, and launch the site — the full content, the feature set, the technical stack, the Render deployment, a phased build plan, and ready-to-use Claude Code prompts.

Prepared as a hand-off document for Claude Code Version 1.0

Target host: Render (Static Site, with an optional Web Service + PostgreSQL upgrade path) Informational document

# Contents

*In Microsoft Word, right-click the table below and choose “Update Field” to populate page numbers.*

# Part I

Project Foundation

## 1. Project Overview & Goals

### 1.1 Vision & Purpose

Rx Automata is a public, vendor-neutral, educational website that explains clearly and authoritatively how two kinds of automation — workflow automation and agentic (AI agent) automation — are transforming the way medicines are discovered, tested, approved, manufactured, distributed, and managed. The goal is a resource that a curious member of the public, a pharmacy student, and a senior pharma decision-maker can all read and come away better informed.

The site should be genuinely useful rather than promotional: explain how the technology actually works, show where it is applied across the life-sciences value chain, present real case studies (including honest failures), and set out what responsible, compliant adoption looks like.

### 1.2 Target Audiences

The content and features must serve several audiences at once. Design the navigation and reading levels so each can find value quickly.

| **Audience** | **What they need** | **How the site serves them** |
|----|----|----|
| Pharma & biotech professionals | Concrete use cases, terminology, current examples | The Value Chain section and Case Studies, with field-specific depth |
| Pharmacy & clinical staff | Medication-management and adherence applications | The Pharmacy Operations section and practical examples |
| Students & educators | Clear, structured explanations of how it all works | “How AI Agents Work” and the glossary; readable, well-structured pages |
| Executives, decision-makers, investors | The “so what” — value, maturity, risks | Outcomes/impact, the Road Ahead, and the responsible-adoption framing |
| General / curious public | Plain-language orientation | A clear home page, jargon defined inline, and a simple narrative arc |

### 1.3 What “Production-Grade” Means Here

Production-grade is not a single feature; it is a set of qualities the finished site must meet. Treat each as a requirement, not a nice-to-have:

- **Reliable hosting & automated deploys —** Hosted on Render with continuous deployment from Git; every push is built and shipped automatically.

- **Responsive —** Works flawlessly on phones, tablets, and desktops.

- **Accessible —** Meets WCAG 2.1 AA so it is usable with keyboards and screen readers.

- **Fast —** Meets Core Web Vitals targets; optimised assets and CDN delivery.

- **Discoverable —** Full SEO: metadata, social cards, structured data, sitemap, semantic markup.

- **Secure —** HTTPS everywhere, sensible security headers, protected forms, validated input.

- **Measured —** Privacy-friendly analytics, uptime monitoring, and error tracking in place.

- **Maintainable —** Clean, component-based code; content easy to update; this document kept in the repo.

- **Compliant & honest —** A privacy policy, a clear informational disclaimer, and accurate, sourced content.

### 1.4 Success Metrics

Define success up front so the build can be evaluated against it:

1.  Lighthouse scores of 90+ for Performance, Accessibility, Best Practices, and SEO.

2.  Core Web Vitals in the “good” range on mobile (see §8.8).

3.  Growing organic search traffic to the value-chain and case-study pages.

4.  Engagement: average time on page and use of the interactive value-chain explorer.

5.  Newsletter sign-ups and contact-form submissions (if those features are enabled).

6.  Uptime at or above 99.9%, monitored continuously.

### 1.5 How to Use This Document with Claude Code

This document is the single source of truth for the build. Recommended workflow:

1.  Put this specification in the repository (for example at /docs/SPEC.md or alongside the project as a reference) so Claude Code can read it.

2.  Create a short CLAUDE.md at the repo root summarising the tech stack, conventions, file structure, and “do/don’t” rules so every Claude Code session shares the same context.

3.  Build in the phases described in Section 11, feeding Claude Code one phase at a time rather than the whole site at once.

4.  Use the ready-made prompts in Section 12 to kick off each phase.

5.  Commit frequently, review the diffs Claude Code proposes before approving them, and deploy to Render after each phase to catch issues early.

# Part II

Content Master — The Substance of the Site

## 2. Foundations: How the Two Automations Work

### 2.1 Workflow Automation (the deterministic pipeline)

Workflow automation is software that moves structured work between systems and people along a path defined in advance — essentially “if this, then that” at scale. A trigger (a new file, a form submission, a scheduled time) starts a sequence of predetermined steps that copy data, transform it, route it for approval, and update other systems.

**How it works.** It connects applications through their APIs (the integration approach) or, when a system has no API, by driving its on-screen interface the way a person would — the approach known as Robotic Process Automation (RPA). The logic is fixed and explicit; the same input always produces the same output.

**Common tools.** Integration platforms such as Zapier, Make, Microsoft Power Automate, and n8n; RPA platforms such as UiPath; and purpose-built, compliance-oriented workflow tools used inside regulated industries.

**Strengths.** Predictable, repeatable, high-volume, and — critically for pharma — auditable by design, with signed steps and immutable history.

**Limits.** It is brittle at the edges. Ambiguous input, exceptions, and judgement calls break the flow, and a human has to step in. It executes rules; it does not interpret them.

### 2.2 Agentic Automation (the reasoning operator)

Agentic automation uses AI agents — systems built around large language models (LLMs) — that interpret a goal, plan the steps to achieve it, call the tools they need, and execute multi-step work with minimal supervision. The key shift is from the “read path” (analysing information) to the “write path” (taking action in real systems): booking, filing, reconciling, drafting, and updating systems of record.

Where workflow automation needs every branch defined ahead of time, an agent can handle situations it was not explicitly scripted for by reasoning about them — which is why the two are complementary rather than competing.

### 2.3 How an AI Agent Actually Works (the anatomy)

An AI agent is best understood as a small set of components working in a loop. Knowing these parts makes the rest of this document — and the interactive diagram the site will feature — much clearer.

- **The model (the “brain”) —** A large language model that interprets instructions, reasons about the task, and decides what to do next.

- **The goal / instructions —** A clear objective plus guardrails: what to achieve, what is out of bounds, and when to ask a human.

- **Tools (function calling) —** The actions the agent can take — search a database, query an API, send an email, run code, file a report. The model chooses which tool to call and with what inputs.

- **Memory —** Short-term context within the current task, plus optional long-term memory stored in a vector database so the agent can recall earlier information.

- **Retrieval-Augmented Generation (RAG) —** A way to ground the agent’s answers in trusted, current, and proprietary documents (for example a company’s own SOPs or safety data) instead of relying only on what the model learned in training.

- **Guardrails & validation —** Safety checks that constrain the agent’s actions, validate its outputs, and stop unsafe or out-of-scope behaviour.

These pieces operate in a repeating cycle often called the reason–act loop:

1.  Observe — take in the goal and any new information or tool results.

2.  Reason / plan — decide the next step toward the goal.

3.  Act — call a tool or produce an output.

4.  Observe the result — read what came back.

5.  Repeat — continue the cycle until the goal is met or a human is asked to step in.

### 2.4 Multi-Agent Systems & Orchestration

Complex work is rarely handled by a single agent. Instead, an orchestrator (or “supervisor”) agent coordinates several specialist agents, each focused on one part of the job, and combines their results. In drug discovery, for example, a production multi-agent framework has used a Supervisor agent alongside Molecule, Lab, Analysis, and Report agents, with a separate Safety Guardrail overseeing the whole system.

**Why multi-agent.** It lets a hard problem be broken into focused sub-tasks, allows each agent to specialise, and enables steps to run in parallel — while the supervisor keeps the overall goal coherent.

### 2.5 Human-in-the-Loop

In regulated and clinical settings, agents are designed to augment expert judgement, not replace it. The most credible systems route consequential decisions — a medical assessment, a regulatory sign-off, a clinical recommendation — to a qualified human, and improve over time through that human feedback. This principle should be visible throughout the site’s content.

### 2.6 How the Two Engines Combine

The mature pattern is not one or the other but both layered together: agents reasoning on top, deterministic workflows and RPA executing underneath, and humans reviewing the decisions that carry weight. Industry analysts now describe a converging category in which integration platforms, RPA, and AI agents merge — making flexible, multi-capability strategies more resilient than single-vendor bets.

### 2.7 Decision Framework: Which Engine, and When

This framework is also the basis for an interactive “Which automation do I need?” tool on the site (see §8.2).

| **Reach for workflow automation when…** | **Reach for agentic automation when…** |
|----|----|
| The process is well-defined, structured, and high-volume | Inputs are unstructured, ambiguous, or vary case by case |
| The rules are stable and rarely change | Exceptions and edge cases are frequent, not rare |
| You need deterministic, repeatable, fully auditable output | The task spans many tools and steps toward a goal |
| The systems have APIs (or RPA can drive their screens) | Success needs reasoning over messy data, not just moving it |

**The rule of thumb.** When in doubt, combine them — and keep a human in the loop wherever the stakes are clinical or regulatory.

## 3. The Pharma & Medicine Value Chain — Use Cases by Field

This is the core of the website. For each of seven stages, the content follows the same pattern: the problem, what workflow automation does, what agentic automation does and how the agent works in that field, real examples, and measurable impact. Each stage should become its own page (or an expandable panel within an interactive explorer).

### 3.1 Drug Discovery & R&D

**The problem.** The slowest, most failure-prone stage. Roughly 90% of candidates fail in clinical development, and the average cost to bring a medicine to market is around \$2.3 billion. Historically, scientists spent their days compiling data and screening thousands of molecules by hand.

### Workflow automation here.

- Automated data pipelines and electronic lab notebooks replacing manual capture

- Harmonised data definitions across pre-clinical and clinical teams

- Lab-instrument integration and orchestration of high-throughput screening

### Agentic automation here — how the agent works.

- Multi-agent systems run the Design–Make–Test–Analyze (DMTA) cycle with minimal supervision

- Agents generate hypotheses, prioritise targets, and design candidate compounds in silico

- They predict efficacy, ADMET properties, and toxicity before a molecule is ever synthesised

- An “AI co-scientist” proposes and refines hypotheses, with expert humans validating

**In practice.** Insilico Medicine nominated a preclinical candidate after screening only 78 molecules; research frameworks such as CoScientist, ChemCrow, and DrugAgent orchestrate cheminformatics and machine-learning tools end to end.

**Measurable impact.** Some analyses report AI-discovered molecules reaching Phase I success rates of roughly 80–90%, well above the historical 40–65%, though later-stage data is still limited.

### 3.2 Clinical Trials & Development

**The problem.** The single costliest, most bottlenecked phase — and one spread across many global sites, each with its own systems and data to provision.

### Workflow automation here.

- Electronic Data Capture (EDC) replacing manual patient-data entry

- Monitoring-visit scheduling and multi-site user provisioning

- Continuous regulatory-compliance tracking across geographies

### Agentic automation here — how the agent works.

- AI-driven patient recruitment that matches eligible participants faster

- Eligibility screening reasoned against electronic health records

- Real-time safety monitoring and autonomous resolution of data queries

- Unified budgeting, contracting, and forecasting for trial finances

**In practice.** Sponsors increasingly pair EDC systems with AI recruitment and monitoring tools to hit enrolment targets and keep data clean across sites.

**Measurable impact.** Faster enrolment and cleaner data attack the two factors that most often blow trial timelines and budgets.

### 3.3 Regulatory Affairs & Submissions

**The problem.** The “regulatory war room” — cross-functional teams scrambling for weeks to cross-check data for global filings to agencies such as the FDA and EMA.

### Workflow automation here.

- Automated generation and validation of submission-ready documents

- Fewer manual formatting errors and faster review cycles

- Records held to agency compliance standards by construction

### Agentic automation here — how the agent works.

- Instant cross-document data verification across a global dossier

- Compliance built into the workflow from day one rather than bolted on at the end

- Humans shift from clerical cross-checking to high-level strategic review

**In practice.** Vendors describe an “augmented regulatory worker” model in which AI, NLP, and RPA handle the mechanical work while regulatory experts focus on strategy.

**Measurable impact.** The aim is not to remove the regulatory expert but to stop them being a data compiler and free them to be a strategist.

### 3.4 Pharmacovigilance & Drug Safety

**The problem.** The flagship automation use case in pharma. Thousands of adverse events are processed every month, each a regulated case with strict timelines under standards such as ICH E2B(R3) and 21 CFR.

### Workflow automation here.

- Case intake from email, portals, and ICSR XML into a central safety database

- Triage, booking, data entry, automated MedDRA coding, and duplicate detection

- Follow-up tracking, SOP-enforcing steps, and a full audit log of every change

- Compliant electronic signature on case review (as in safety platforms such as Argus)

### Agentic automation here — how the agent works.

- Agents extract adverse events from unstructured sources — literature, calls, social media

- They draft case narratives and perform a first-pass medical assessment

- They surface safety signals and route complex cases for human medical review

**In practice.** Industrial pharmacovigilance operations and their outsourcing partners process individual case safety reports (ICSRs) at scale; established safety databases automate coding, duplicate detection, and audit trails.

**Measurable impact.** Rising data volumes, faster approvals, and global rule nuances make manual case handling unsustainable — exactly the gap intelligent automation fills.

### 3.5 Manufacturing & Quality (GxP)

**The problem.** Where consistency is everything. A single out-of-specification batch is costly waste — and a compliance event.

### Workflow automation here.

- Process Analytical Technology (PAT) monitoring production parameters in real time

- Automated batch records and deviation management

- Closed-loop CAPA workflows that document and resolve quality issues

### Agentic automation here — how the agent works.

- Anomaly detection across complex, multi-source manufacturing data

- Reasoned root-cause analysis on deviations before they cascade

- Predictive quality that flags drift toward control limits early

**In practice.** Manufacturers combine PAT and automated batch records with analytics to keep conditions within control limits and reduce batch failures.

**Measurable impact.** Every automated GxP step must be validated to perform exactly as intended, with any deviation immediately detectable.

### 3.6 Supply Chain & Distribution

**The problem.** Getting the right medicine to the right place, on time, at the right temperature — across a fragile, globally distributed network.

### Workflow automation here.

- Automated inventory, purchasing, and order processing

- Demand signals unified across previously siloed data

- Reduced reliance on manual intervention as operations scale

### Agentic automation here — how the agent works.

- Digital twins that simulate the chain to test decisions before deployment

- Dynamic rerouting around weather, customs, and capacity — within Good Distribution Practice (GDP)

- Anticipating shortages, monitoring price swings, and checking contract adherence

**In practice.** Pharma logistics is moving toward autonomous planning systems, AI control towers, and digital twins, increasingly integrated with IoT and blockchain.

**Measurable impact.** The emerging 2026 standard is interoperable, explainable, and audit-ready AI decisions across the chain.

### 3.7 Pharmacy Operations & Medication Management

**The problem.** The “management medicine” frontier, where automation meets the patient. The most clinically validated win is medication adherence; the biggest time-saver is freeing pharmacists from administrative load.

### Workflow automation here.

- Dispensing robotics and automated inventory management

- Prescription processing — refills, transfers, and new requests

- Automated refill reminders and routine patient communications

### Agentic automation here — how the agent works.

- Agents process prescriptions and update the pharmacy management system in real time

- Insurance verification, copay and coverage queries, and inbound call handling

- Outbound adherence and vaccination campaigns; medication reconciliation that flags discrepancies

- OCR that reads handwritten prescriptions; adherence sensed via smart bottles, dispensers, and wearables

**In practice.** Purpose-built pharmacy agents handle calls, refills, insurance checks, and adherence outreach; adherence monitoring is widely regarded as the most validated and scalable AI opportunity in pharmacy practice.

**Measurable impact.** One platform reported roughly a 67% reduction in administrative processing time — the recurring principle is that AI automates low-value tasks so clinical judgement and patient care get the human hours.

## 4. Case Studies — Real Deployments, Honest Limits

Present these as filterable cards on the site (see §8.2). Include the cautionary case deliberately: credibility comes from honesty about what does not work.

| **Organisation** | **Domain** | **What they did** | **Outcome / lesson** |
|----|----|----|----|
| Insilico Medicine | Discovery | Used a generative chemistry platform to design a candidate for idiopathic pulmonary fibrosis | Candidate after only ~78 molecules; later reported positive Phase IIa results |
| Exscientia × Sumitomo | Discovery (caution) | Designed DSP-1181, an AI-designed molecule for OCD, into human trials in under a year | Discontinued after Phase I despite a favourable safety profile — speed ≠ success |
| Recursion | Discovery | Automated high-throughput cellular imaging paired with deep learning | Industrialised phenotypic screening for discovery and repurposing |
| GSK; Eli Lilly | Discovery (signal) | Signed access deals for oncology and drug-design foundation models (early 2026) | Big pharma moving AI-native discovery from fringe to core |
| Argus-class safety systems | Pharmacovigilance | Central safety databases with auto MedDRA coding, duplicate detection, audit trails | Regulated backbone processing thousands of cases per month |
| AI pharmacy agents | Medication mgmt | Handle calls, refills, insurance checks, reconciliation, OCR of scripts | ~67% reported cut in administrative processing time |

## 5. Responsible & Compliant Adoption

In medicine, “it mostly works” is not good enough. These non-negotiables separate a deployable system from a liability, and they should be a prominent section of the site.

- **Validate everything —** Every automated workflow, however minor, must be validated to perform exactly as intended under 21 CFR Part 11, GCP, GLP, and GMP, with deviations immediately detectable.

- **Audit trails & e-signatures —** Signed steps, immutable history, and design snapshots make a process independently auditable — the difference between speed and a finding in an inspection.

- **Keep humans in the loop —** Agents augment clinical and regulatory judgement; they do not replace it. Route decisions of consequence to a qualified human.

- **Harmonise the data first —** Inconsistent field labels and units cause silent errors — such as matching patient data to the wrong treatment arm. Clean definitions come before automation.

- **Govern, upskill, protect equity —** Governance-first design, workforce training, and equity safeguards must be built in from the start, not retrofitted after something goes wrong.

- **Acknowledge the limits —** AI accelerates discovery but does not guarantee clinical success, and it struggles to replace clinical judgement or work cleanly across disparate data sources.

|  |
|----|
| **The honest takeaway (use as a pull-quote)** |
| *AI performs best when it automates well-defined workflows, and falls short when asked to replace clinical judgement. Deterministic workflows for the structured majority, agents for the ambiguous middle, and humans wherever the stakes are highest.* |

## 6. The Road Ahead

The near-term trajectory is less about flashier chatbots and more about automation moving upstream — into prediction, planning, and orchestration.

- **R&D → R&P —** A shift from Research & Development to Research & Prediction: simulating outcomes digitally so only the highest-quality candidates consume lab time or trial budget.

- **AI-native discovery as default —** Projections suggest more than half of new drugs could be discovered using AI methods by 2030.

- **Self-driving supply chains —** Autonomous planning, AI control towers, and digital twins become standard, with audit-ready decisions by default.

- **One converged platform layer —** The boundaries between integration, RPA, and agents keep dissolving, pushing teams toward flexible, multi-capability stacks.

- **Compliance built in from day one —** Agentic systems increasingly fold verification into the workflow itself, turning the regulatory scramble into continuous assurance.

- **The human stays central —** Across discovery, safety, and the pharmacy counter, the durable role of automation is to remove drudgery and hand expert time back to expert judgement.

# Part III

Website Specification — Features & Functionality

## 7. Information Architecture

The recommended site map. Keep the structure shallow and the navigation obvious. Each row below is a page or major view.

| **Page** | **Purpose** | **Key content / sections** |
|----|----|----|
| Home | Orient any visitor in seconds and route them onward | Hero, the two-engines summary, value-chain preview, featured case study, CTAs |
| What Is Automation? | Explain workflow vs agentic clearly | Section 2.1–2.2 and 2.6–2.7, with the comparison and the decision framing |
| How AI Agents Work | Teach the mechanics | Section 2.3–2.5, anchored by an interactive agent-architecture diagram |
| The Value Chain | The core: applications across pharma | Interactive explorer covering all seven stages from Section 3 |
| Use Cases by Field | Deep dives per stage | One page per stage (3.1–3.7), or expandable panels within the explorer |
| Case Studies | Proof, including honest limits | Filterable cards from Section 4 |
| Responsible Adoption | Compliance and ethics | Section 5, with the pull-quote and the non-negotiables |
| The Road Ahead | Forward view | Section 6, optionally a timeline |
| Insights / Blog | Keep the site fresh for SEO | Article index and posts (optional, but recommended for organic growth) |
| Resources / Glossary | Reference | Glossary (Appendix A), downloadable summary, links |
| About | Trust and context | Purpose, scope, methodology, the informational disclaimer |
| Contact | Let people reach you | Contact form and, optionally, newsletter sign-up |

## 8. Feature Specification

Features are tagged by priority: Must (launch blocker), Should (important, near-term), Could (enhancement). Build Must items first.

### 8.1 Global & Core

| **Feature** | **Description** | **Priority** |
|----|----|----|
| Responsive layout | Mobile-first; fluid grid; tested at common breakpoints | Must |
| Primary navigation | Clear header nav with current-section highlighting; mobile menu | Must |
| Footer | Sitemap links, disclaimer, privacy link, back-to-top | Must |
| Consistent design system | Tokens for colour, type, spacing; reusable components | Must |
| Dark / light theme | Respects system preference; toggle persists per session | Should |
| Breadcrumbs | On deep pages (e.g. value-chain stages) | Should |
| 404 & error pages | Friendly, on-brand, with navigation back | Must |

### 8.2 Interactive Features

| **Feature** | **Description** | **Priority** |
|----|----|----|
| Value-chain explorer | Interactive seven-stage map; each opens workflow/agentic detail | Must |
| Agent-architecture diagram | Animated, labelled diagram of how an agent works (§2.3) | Should |
| “Which automation?” tool | Short guided questions return workflow vs agentic guidance (§2.7) | Should |
| Filterable case studies | Filter cards by domain and by success/cautionary | Should |
| Glossary tooltips | Hover/tap definitions for jargon inline in the text | Could |
| Comparison tables | Reusable, accessible table component for side-by-side content | Must |
| Timeline | Optional visual timeline for the Road Ahead | Could |

### 8.3 Content Features

| **Feature** | **Description** | **Priority** |
|----|----|----|
| Markdown / content collections | Author pages and posts as content files, not hard-coded HTML | Must |
| Insights / blog | Indexed article list with tags and RSS | Should |
| Resource downloads | Downloadable PDF summary / one-pager | Could |
| FAQ | Common questions with structured-data markup | Should |

### 8.4 Engagement & Conversion

| **Feature** | **Description** | **Priority** |
|----|----|----|
| Contact form | Validated, spam-protected; emails or stores submissions | Must |
| Newsletter sign-up | Double opt-in; stores email securely (needs backend / service) | Should |
| Clear CTAs | Purposeful calls to action on key pages | Must |
| Social sharing | Share links with correct preview cards | Could |

### 8.5 Search

Add on-site search so visitors can jump to a stage, term, or case study. For a static site, a client-side index (for example Pagefind or a lightweight Lunr/Fuse index built at build time) avoids needing a backend. Priority: Should.

### 8.6 Accessibility (WCAG 2.1 AA)

- Semantic HTML landmarks (header, nav, main, footer) and a logical heading order.

- Full keyboard operability with a visible focus indicator; a “skip to content” link.

- Colour contrast of at least 4.5:1 for body text; never rely on colour alone.

- Descriptive alt text for images and accessible names for interactive controls.

- ARIA only where needed (e.g. the explorer and tooltips); respect reduced-motion preferences.

- Test with a screen reader and an automated checker (axe / Lighthouse).

### 8.7 SEO

- Unique, descriptive title and meta description per page.

- Open Graph and Twitter card tags for rich social previews.

- JSON-LD structured data (Organization, Article, FAQ, BreadcrumbList where relevant).

- Auto-generated sitemap.xml and a sensible robots.txt.

- Canonical URLs, clean human-readable slugs, and semantic markup.

- Descriptive alt text and meaningful internal linking between related pages.

### 8.8 Performance (Core Web Vitals)

Targets to meet on mobile:

| **Metric** | **Target** | **How** |
|----|----|----|
| Largest Contentful Paint (LCP) | \< 2.5 s | Optimised hero, preloaded fonts, CDN delivery |
| Interaction to Next Paint (INP) | \< 200 ms | Minimal JavaScript; defer non-critical scripts |
| Cumulative Layout Shift (CLS) | \< 0.1 | Set image/embed dimensions; reserve space |

- Serve modern image formats (WebP/AVIF), correctly sized, lazy-loaded below the fold.

- Minify and bundle CSS/JS; ship as little JavaScript as possible.

- Use the host CDN and sensible cache headers for static assets.

- Subset and self-host or preconnect fonts to avoid render-blocking.

### 8.9 Analytics & Monitoring

- Privacy-friendly analytics (e.g. Plausible or a properly configured GA4) with a cookie notice if required.

- Event tracking on key interactions: explorer opens, decision-tool completion, CTA clicks, form submits.

- Uptime monitoring with alerting.

- Error tracking (e.g. Sentry) for client and any server code.

### 8.10 Security & Privacy

- HTTPS/TLS everywhere (automatic on Render).

- Security headers: Content-Security-Policy, HSTS, X-Content-Type-Options, Referrer-Policy.

- Form protection: honeypot field plus a privacy-respecting CAPTCHA and/or rate limiting.

- Validate and sanitise all input; never trust client data.

- A clear privacy policy and cookie notice; handle any stored personal data per GDPR-style principles.

- Keep dependencies patched; never commit secrets — use environment variables.

# Part IV

Technical Build & Deployment on Render

## 9. Recommended Tech Stack & Architecture

### 9.1 Option A — Static Site (recommended starting point)

For an informational site like this, a static site is the fastest, cheapest, and most robust choice, and it deploys free on Render with a global CDN and automatic TLS. Recommended approach:

- Framework: Astro (content-focused, very fast, ships minimal JavaScript, supports interactive “islands” for the explorer and diagram). Eleventy or a Next.js static export are reasonable alternatives.

- Styling: Tailwind CSS or well-structured vanilla CSS with design tokens.

- Content: Markdown / MDX content collections so pages are easy to edit.

- Forms: a form-handling service or a tiny serverless function so no full backend is needed at launch.

### 9.2 Option B — Full-Stack (only when you need stored data)

Move to this when you add features that must store or query data — newsletter sign-ups, contact messages saved to a database, or server-side search.

- Frontend: the same Astro/React front end.

- Backend: a Node service (Express, or Next.js API routes) deployed as a Render Web Service.

- Database: Render PostgreSQL for submissions and any structured data.

- Note: Render’s free web services spin down when idle, so the first request after inactivity has a cold-start delay; a paid instance removes this.

### 9.3 Recommendation

Start with Option A and deploy as a Render Static Site. Add a Render Web Service plus PostgreSQL (Option B) only when a data-storing feature genuinely requires it. This keeps the launch simple, free, and fast, while leaving a clean upgrade path — Render is a single platform that hosts both, so you will not need to migrate.

### 9.4 Suggested Repository Structure

| **Path** | **Contents** |
|----|----|
| /CLAUDE.md | Project conventions and context for Claude Code |
| /docs/SPEC.md | This specification |
| /render.yaml | Render Blueprint defining the service(s) as code |
| /package.json | Dependencies and build/start scripts |
| /src/pages/ | Route pages (home, value-chain stages, case studies, etc.) |
| /src/components/ | Reusable UI (nav, footer, explorer, diagram, cards, tables) |
| /src/content/ | Markdown content collections (stages, case studies, posts) |
| /src/styles/ | Design tokens and global styles |
| /public/ | Static assets: images, favicon, robots.txt |

## 10. Deploying on Render

### 10.1 Static Site

1.  Push the repository to GitHub (or GitLab/Bitbucket).

2.  In the Render dashboard choose New → Static Site and connect the repository.

3.  Set the Build Command (for Astro, npm run build) and the Publish Directory (for Astro, dist).

4.  Click Create Static Site — Render runs the first deploy and serves the site over its global CDN with automatic TLS, at a unique onrender.com URL.

5.  Every push to the chosen branch then triggers an automatic rebuild and deploy.

*Static sites count against the workspace’s included monthly outbound bandwidth and build (“pipeline”) minutes; usage is visible in the dashboard.*

### 10.2 Web Service (only if you add a backend)

1.  Choose New → Web Service and connect the repository; Render auto-detects the Node runtime.

2.  Set the build command (e.g. npm install && npm run build) and the start command (e.g. npm start).

3.  Add environment variables for any secrets and the database connection string.

4.  Create the service. The free tier provides 750 instance-hours per month — enough to keep one service running full time — but free services sleep when idle and cold-start on the next request.

### 10.3 Custom Domain & SSL

In the site’s settings, add your custom domain, then create the CNAME record Render shows you at your domain registrar. Render provisions and renews a managed TLS certificate automatically. Hobby workspaces include two custom domains at no extra cost (additional domains are a small monthly fee).

### 10.4 Environment Variables, Auto-Deploy & Previews

- Store all secrets (API keys, database URLs) as environment variables — never in the code.

- Auto-deploy on push is on by default for the branch you select.

- Pull-request previews let you review changes on a temporary URL before merging.

### 10.5 Blueprint (render.yaml)

Define your services as code so deploys are reproducible. A minimal static-site Blueprint looks like this (your build command and publish path may differ by framework):

|                                            |
|--------------------------------------------|
| **render.yaml — static site**              |
| *services:                                 
 - type: web                                 
 name: rx-automata                           
 runtime: static                             
 buildCommand: npm install && npm run build  
 staticPublishPath: ./dist                   
 autoDeploy: true*                           |

## 11. Build Roadmap — Phased Plan for Claude Code

Build in order. Deploy to Render at the end of Phase 0 and after each subsequent phase so problems surface early.

Phase 0 — Setup & Pipeline

**Goal.** Get a deployable skeleton live on Render to prove the workflow end to end.

### Deliverables.

- Initialise the repo, the Astro project, CLAUDE.md, and /docs/SPEC.md

- Add base tooling (formatting, linting)

- Deploy a placeholder static site to Render and confirm auto-deploy works

Phase 1 — Design System & Layout

**Goal.** Establish the look and the shared shell.

### Deliverables.

- Define design tokens (colours, typography, spacing)

- Build the global layout, header navigation, and footer

- Implement responsive behaviour and dark/light theme

Phase 2 — Core Content Pages

**Goal.** Populate the substance from Part II.

### Deliverables.

- Home, What Is Automation, How AI Agents Work

- Value-Chain overview plus the seven stage pages (3.1–3.7)

- Case Studies, Responsible Adoption, The Road Ahead

Phase 3 — Interactive Features

**Goal.** Add the features that make the site memorable.

### Deliverables.

- Value-chain explorer

- Agent-architecture diagram

- “Which automation?” decision tool and filterable case studies

Phase 4 — Engagement & Data (optional backend)

**Goal.** Add contact and newsletter; introduce a backend only if storing data.

### Deliverables.

- Contact form with validation and spam protection

- Newsletter sign-up

- If storing submissions: add a Render Web Service and PostgreSQL (Option B)

Phase 5 — SEO, Accessibility & Performance

**Goal.** Make it discoverable, usable, and fast.

### Deliverables.

- Metadata, Open Graph, JSON-LD, sitemap, robots.txt

- Accessibility pass against the §8.6 checklist

- Lighthouse optimisation to hit the Core Web Vitals targets

Phase 6 — Analytics, Security & Monitoring

**Goal.** Instrument and harden the site.

### Deliverables.

- Analytics and event tracking

- Security headers, form protection, privacy policy

- Uptime monitoring and error tracking

Phase 7 — Launch & Iterate

**Goal.** Go live and keep improving.

### Deliverables.

- Connect the custom domain; final QA against the pre-launch checklist (Appendix C)

- Launch

- Iterate with insights/blog posts and content updates

## 12. Ready-to-Use Claude Code Prompts

Paste these into Claude Code to start each phase. Adjust names and choices to taste. Always review proposed changes before approving them.

|  |
|----|
| **Phase 0 — scaffold** |
| *Read /docs/SPEC.md. Scaffold a new Astro static site for the project described there. Create a CLAUDE.md capturing our stack (Astro, Tailwind, Markdown content collections), file structure, and conventions. Add a render.yaml Blueprint for a Render Static Site. Set up Prettier and ESLint. Give me a placeholder home page so I can deploy to Render and confirm the pipeline.* |

|  |
|----|
| **Phase 1 — design system** |
| *Using the brand in /docs/SPEC.md (apothecary green, signal amber, warm paper, an editorial serif for headings and a clean sans for body), create design tokens, a global layout, a responsive header nav with current-section highlighting, a footer, and a dark/light theme toggle. Keep it accessible and ship minimal JavaScript.* |

|  |
|----|
| **Phase 2 — content pages** |
| *From Part II of /docs/SPEC.md, build the core pages as Markdown content collections: Home, What Is Automation, How AI Agents Work, the Value-Chain overview, the seven stage pages (3.1–3.7), Case Studies, Responsible Adoption, and The Road Ahead. Use a reusable, accessible comparison-table component for the side-by-side content.* |

|  |
|----|
| **Phase 3 — interactivity** |
| *Build an interactive value-chain explorer covering the seven stages (each opening its workflow and agentic detail), an animated agent-architecture diagram based on §2.3, and a short “Which automation do I need?” guided tool based on §2.7. Make all of it keyboard-accessible and respect reduced-motion.* |

|  |
|----|
| **Phase 5 — SEO & a11y & perf** |
| *Add per-page titles and meta descriptions, Open Graph and Twitter cards, JSON-LD (Organization, Article, FAQ, BreadcrumbList), a generated sitemap.xml and robots.txt. Then run an accessibility and Lighthouse pass and fix issues until Performance, Accessibility, Best Practices, and SEO are all 90+ on mobile, meeting the Core Web Vitals targets in §8.8.* |

|  |
|----|
| **Phase 6 — hardening** |
| *Add privacy-friendly analytics with event tracking on the explorer, decision tool, and CTAs; configure security headers (CSP, HSTS, X-Content-Type-Options, Referrer-Policy); add a privacy policy and cookie notice; and wire up error tracking. Protect the contact form with a honeypot, rate limiting, and a privacy-respecting CAPTCHA.* |

# Appendices

Reference Material

Appendix A — Glossary

| **Term** | **Meaning** |
|----|----|
| Agent | An AI system that interprets a goal, plans, uses tools, and acts with minimal supervision. |
| Agentic automation | Automation driven by such agents, capable of reasoning through ambiguity and exceptions. |
| Workflow automation | Rule-based automation that moves structured work along a predefined path. |
| RPA | Robotic Process Automation — software that drives on-screen interfaces of systems that lack APIs. |
| iPaaS | Integration Platform as a Service — cloud tools that connect apps via their APIs (e.g. Zapier, Make). |
| LLM | Large Language Model — the AI model at the core of a modern agent. |
| RAG | Retrieval-Augmented Generation — grounding an AI’s answers in trusted, retrieved documents. |
| Reason–act loop | The observe → reason → act → observe cycle an agent repeats until its goal is met. |
| Multi-agent system | Several specialised agents coordinated by a supervisor agent. |
| Human-in-the-loop (HITL) | Routing consequential decisions to a qualified human for review or approval. |
| MCP | Model Context Protocol — an emerging standard for connecting AI models to tools. |
| ICSR | Individual Case Safety Report — the regulated record of an adverse event. |
| MedDRA | Standardised medical terminology used to code adverse events. |
| Pharmacovigilance (PV) | The science of detecting, assessing, and preventing adverse drug effects. |
| GxP | Umbrella for “Good x Practice” regulations (manufacturing, clinical, laboratory, distribution). |
| 21 CFR Part 11 | FDA rule governing electronic records and electronic signatures. |
| DMTA cycle | Design–Make–Test–Analyze — the iterative loop of drug discovery. |
| ADMET | Absorption, Distribution, Metabolism, Excretion, Toxicity — properties predicted for drug candidates. |
| PAT | Process Analytical Technology — real-time monitoring of manufacturing parameters. |
| CAPA | Corrective and Preventive Action — the quality process for resolving issues. |
| GDP | Good Distribution Practice — rules governing pharmaceutical distribution and logistics. |
| EDC | Electronic Data Capture — systems for collecting clinical-trial data. |
| Digital twin | A simulated replica of a physical system (e.g. a supply chain) used to test decisions. |
| Core Web Vitals | Google’s key user-experience metrics: LCP, INP, and CLS. |
| WCAG | Web Content Accessibility Guidelines — the accessibility standard (target: 2.1 AA). |
| SSG / CDN / TLS | Static-Site Generator; Content Delivery Network; Transport Layer Security (HTTPS). |
| CI/CD | Continuous Integration / Continuous Deployment — automatic build-and-ship on every change. |
| Cold start | The delay when a sleeping free web service wakes to serve its first request. |

Appendix B — Content Source Notes & Disclaimer

The content in Part II is synthesised from publicly reported industry sources and analyses from 2025–2026, including life-sciences and AI trade publications, vendor and analyst write-ups, and peer-reviewed and pre-print research. Figures, company examples, and outcomes are illustrative and are not endorsements, guarantees, medical advice, or regulatory guidance. Company names are used for factual reference only and imply no affiliation. Before relying on any specific claim for clinical, regulatory, or investment decisions, verify it against primary sources. Keep this disclaimer reflected in the site’s About page and footer.

Appendix C — Pre-Launch Checklist

Confirm each item before going live:

- Content: every page proofread; disclaimer present; links work.

- Design: responsive on phone/tablet/desktop; dark and light themes correct.

- Accessibility: keyboard-navigable; contrast passes; screen-reader checked; reduced-motion respected.

- SEO: titles, descriptions, OG/Twitter cards, JSON-LD, sitemap.xml, robots.txt all present.

- Performance: Lighthouse 90+; Core Web Vitals in the good range on mobile.

- Security: HTTPS; security headers set; forms protected; no secrets in the repo.

- Analytics & monitoring: analytics live; uptime and error tracking active.

- Legal: privacy policy and cookie notice published.

- Deployment: custom domain connected with TLS; auto-deploy verified; 404 page works.

*End of specification · Rx Automata*
