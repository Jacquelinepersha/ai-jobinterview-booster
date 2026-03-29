"""
Prompts — the real magic. These are heavily optimized for structured, useful output.
Supports English and Spanish (easily extensible to more languages).
"""

SYSTEM_EN = """You are an elite career coach who has helped 10,000+ professionals land jobs at top companies.
You give specific, actionable advice — not generic fluff.
You understand ATS systems, recruiter psychology, and what actually gets interviews."""

SYSTEM_ES = """Eres un coach de carrera de élite que ha ayudado a más de 10,000 profesionales a conseguir trabajo en las mejores empresas.
Das consejos específicos y accionables — nada genérico.
Entiendes los sistemas ATS, la psicología de los reclutadores y lo que realmente consigue entrevistas."""

def get_system(lang="English"):
    return SYSTEM_ES if lang == "Español" else SYSTEM_EN

def _lang_instruction(lang):
    if lang == "Español":
        return "\n\nIMPORTANT: Respond ENTIRELY in Spanish (Español). All headers, analysis, and recommendations must be in Spanish."
    return ""


def job_match_prompt(resume: str, job: str, lang: str = "English") -> str:
    return f"""Analyze how well this candidate matches this job. Be brutally honest.

## JOB DESCRIPTION:
{job}

## CANDIDATE RESUME:
{resume}

Respond in this EXACT format (use the headers exactly as shown):

### MATCH SCORE: [number]/100

### VERDICT: [Strong Match / Good Match / Partial Match / Weak Match]

### YOUR STRENGTHS FOR THIS ROLE:
- [strength 1 — be specific, reference actual resume content]
- [strength 2]
- [strength 3]

### SKILLS YOU'RE MISSING:
- [missing skill 1 — explain why it matters for this role]
- [missing skill 2]

### RED FLAGS:
- [anything that might hurt this application, or "None identified"]

### SALARY ESTIMATE: [estimated range based on role + location + level]

### BOTTOM LINE:
[2-3 sentences: should they apply? what should they emphasize? what to study/learn quickly?]{_lang_instruction(lang)}"""


def resume_optimizer_prompt(resume: str, job: str, lang: str = "English") -> str:
    return f"""Rewrite this resume to be perfectly targeted for this specific job.

## JOB DESCRIPTION:
{job}

## CURRENT RESUME:
{resume}

Rules:
1. Keep ALL factual information unchanged (dates, companies, schools, degrees)
2. Rewrite bullet points to emphasize relevant experience for THIS job
3. Front-load the most relevant experience
4. Add keywords from the job description naturally (not stuffed)
5. Quantify achievements with numbers wherever possible
6. Use strong action verbs that match the job's seniority level
7. Make the professional summary laser-targeted to this role
8. Keep it ATS-friendly: simple formatting, standard section headers
9. Aim for 1-2 pages of content

Respond in this EXACT format:

### OPTIMIZED RESUME:
[the complete rewritten resume in clean format]

### KEYWORDS ADDED:
- [keyword 1] — [where you placed it]
- [keyword 2] — [where you placed it]
- [keyword 3] — [where you placed it]

### WHAT CHANGED AND WHY:
- [change 1 — why this helps]
- [change 2 — why this helps]
- [change 3 — why this helps]{_lang_instruction(lang)}"""


def cover_letter_prompt(resume: str, job: str, company: str = "", lang: str = "English") -> str:
    return f"""Write a cover letter that will make a hiring manager stop scrolling and read the whole thing.

## JOB:
{job}

## CANDIDATE:
{resume}

## COMPANY: {company or 'the company'}

Rules:
1. 250-350 words, 3-4 short paragraphs
2. Opening: a hook that shows you understand their specific challenge or mission — NOT "I'm excited to apply"
3. Body: 2-3 concrete achievements from the resume that directly solve their stated needs, with numbers
4. Show you researched the company — reference something specific about them
5. Closing: confident call to action, not desperate
6. Sound like a real human — vary sentence length, use contractions, have personality
7. NEVER start with "As a [title] with [X] years..."
8. NEVER use "I believe I would be a great fit"
9. NEVER use "I am writing to express my interest in"

Respond with ONLY the cover letter. No labels, no "Dear Hiring Manager" unless it fits naturally. Start with the hook.{_lang_instruction(lang)}"""


def interview_prep_prompt(resume: str, job: str, lang: str = "English") -> str:
    return f"""Generate interview preparation for this specific role.

## JOB:
{job}

## CANDIDATE:
{resume}

Respond in this format:

### LIKELY INTERVIEW QUESTIONS:
1. [question based on the job requirements]
   **How to answer:** [specific guidance using their resume experience]
2. [question]
   **How to answer:** [guidance]
3. [question]
   **How to answer:** [guidance]
4. [question]
   **How to answer:** [guidance]
5. [question]
   **How to answer:** [guidance]

### YOUR "TELL ME ABOUT YOURSELF" ANSWER:
[A 60-second pitch tailored to this exact role, using their actual experience]

### QUESTIONS YOU SHOULD ASK THEM:
1. [smart question that shows you understand the role]
2. [question about team/growth]
3. [question about challenges/impact]

### AREAS TO STUDY BEFORE THE INTERVIEW:
- [topic 1 — why it matters for this role]
- [topic 2]
- [topic 3]{_lang_instruction(lang)}"""


def linkedin_optimizer_prompt(resume: str, job: str, lang: str = "English") -> str:
    return f"""Optimize this person's LinkedIn headline and summary to attract recruiters for this type of role.

## TARGET ROLE:
{job}

## THEIR BACKGROUND:
{resume}

Respond in this format:

### LINKEDIN HEADLINE (max 120 characters):
[headline that includes key role terms + a value proposition]

### LINKEDIN ABOUT SECTION (max 2000 characters):
[a compelling summary that reads naturally, includes searchable keywords, and tells a career story that leads to this target role]

### TOP 5 SKILLS TO LIST:
1. [skill — why recruiters search for this]
2. [skill]
3. [skill]
4. [skill]
5. [skill]

### PROFILE KEYWORDS TO ADD:
[comma-separated list of terms recruiters use to find candidates like this]{_lang_instruction(lang)}"""
