"""
AI Job Interview Booster — Streamlit App
Run: streamlit run app.py
"""
import streamlit as st
import time

# ─── Page config ───────────────────────────────────
st.set_page_config(
    page_title="AI Job Interview Booster",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── Custom CSS ────────────────────────────────────
st.markdown("""
<style>
    /* Clean up defaults */
    .block-container { padding-top: 2rem; max-width: 1100px; }
    
    /* Hero section */
    .hero { text-align: center; padding: 1.5rem 0 1rem; }
    .hero h1 { font-size: 2.4rem; font-weight: 700; margin-bottom: 0.3rem; }
    .hero p { font-size: 1.1rem; opacity: 0.7; margin-top: 0; }
    
    /* Score display */
    .score-box {
        background: linear-gradient(135deg, #1B2A4A 0%, #2E75B6 100%);
        color: white; border-radius: 16px; padding: 2rem;
        text-align: center; margin: 1rem 0;
    }
    .score-box .number { font-size: 3.5rem; font-weight: 800; line-height: 1; }
    .score-box .label { font-size: 1rem; opacity: 0.85; margin-top: 0.5rem; }
    
    /* Feature cards */
    .feature-card {
        background: #f8f9fa; border-radius: 12px; padding: 1.2rem;
        border-left: 4px solid #2E75B6; margin-bottom: 0.8rem;
    }
    .feature-card.green { border-left-color: #0F6E56; }
    .feature-card.orange { border-left-color: #D85A30; }
    .feature-card.purple { border-left-color: #534AB7; }
    
    /* Result area */
    .result-header { 
        font-size: 1.3rem; font-weight: 600; 
        padding-bottom: 0.5rem; border-bottom: 2px solid #2E75B6; 
        margin-bottom: 1rem; 
    }
    
    /* Stat cards row */
    .stat-card { text-align: center; padding: 1rem; border-radius: 10px; background: #f0f2f6; }
    .stat-card .num { font-size: 1.8rem; font-weight: 700; color: #1B2A4A; }
    .stat-card .lbl { font-size: 0.8rem; opacity: 0.6; }
    
    /* Sidebar */
    .sidebar-badge {
        background: #EAF3DE; color: #0F6E56; padding: 0.3rem 0.7rem;
        border-radius: 20px; font-size: 0.75rem; font-weight: 600;
        display: inline-block; margin-bottom: 0.5rem;
    }
    
    /* Hide streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display:none;}
</style>
""", unsafe_allow_html=True)


# ─── Sidebar ───────────────────────────────────────
with st.sidebar:
    st.markdown('<div class="sidebar-badge">✨ FREE TO USE</div>', unsafe_allow_html=True)
    st.markdown("## ⚙️ Settings")
    
    # Language selector
    lang = st.radio("🌐 Language / Idioma", ["English", "Español"], index=0)
    
    st.divider()
    
    # API key input
    api_source = st.radio("AI Provider", ["OpenAI", "Anthropic Claude", "Ollama (Free Local)"], index=0)
    
    if api_source == "OpenAI":
        api_key = st.text_input("OpenAI API Key", type="password", placeholder="sk-...")
        if api_key:
            import os
            os.environ["OPENAI_API_KEY"] = api_key
    elif api_source == "Anthropic Claude":
        api_key = st.text_input("Anthropic API Key", type="password", placeholder="sk-ant-...")
        if api_key:
            import os
            os.environ["ANTHROPIC_API_KEY"] = api_key
    else:
        st.info("Make sure Ollama is running locally" if lang == "English" else "Asegúrate de que Ollama esté corriendo localmente")
        import os
        os.environ.pop("OPENAI_API_KEY", None)
        os.environ.pop("ANTHROPIC_API_KEY", None)
    
    st.divider()
    
    if lang == "English":
        st.markdown("### 📊 How to use")
        st.markdown("""
        1. **Paste** your resume below
        2. **Paste** a job description
        3. **Pick** a tool from the tabs
        4. **Click** the button — done!
        
        💡 *Each result is tailored to that specific job*
        """)
    else:
        st.markdown("### 📊 Cómo usar")
        st.markdown("""
        1. **Pega** tu currículum abajo
        2. **Pega** una descripción de trabajo
        3. **Elige** una herramienta
        4. **Haz clic** en el botón — ¡listo!
        
        💡 *Cada resultado se adapta a ese trabajo específico*
        """)
    
    st.divider()
    st.markdown("### 💰 Cost per use" if lang == "English" else "### 💰 Costo por uso")
    st.markdown("""
    | Action | Cost |
    |--------|------|
    | Job Match | ~$0.01 |
    | Resume Optimize | ~$0.02 |
    | Cover Letter | ~$0.01 |
    | Interview Prep | ~$0.01 |
    | LinkedIn Optimize | ~$0.01 |
    """)
    st.caption("Prices based on GPT-4o-mini. Claude may vary slightly." if lang == "English" else "Precios basados en GPT-4o-mini. Claude puede variar.")


# ─── UI text based on language ─────────────────────
T = {
    "English": {
        "hero_title": "🚀 AI Job Interview Booster",
        "hero_sub": "Paste your resume + a job description → get tailored materials in seconds",
        "resume_label": "#### 📄 Your Resume",
        "resume_placeholder": "Paste your resume text here...\n\nInclude: name, experience, skills, education",
        "job_label": "#### 💼 Job Description",
        "job_placeholder": "Paste the full job posting here...\n\nInclude: title, requirements, responsibilities",
        "company_label": "🏢 Company name (optional — improves cover letter personalization)",
        "company_placeholder": "e.g., Stripe, Google, Acme Corp",
        "warn_resume": "⚠️ Please paste your resume (at least a few sentences)",
        "warn_job": "⚠️ Please paste the job description (at least a few sentences)",
        "warn_key": "🔑 Please enter your API key in the sidebar",
        "tab_match": "🧠 Job Match Score",
        "tab_resume": "✍️ Optimize Resume",
        "tab_cover": "📄 Cover Letter",
        "tab_interview": "🎤 Interview Prep",
        "tab_linkedin": "💼 LinkedIn Optimizer",
        "btn_match": "🧠 Analyze My Match",
        "btn_resume": "✍️ Optimize My Resume",
        "btn_cover": "📄 Generate Cover Letter",
        "btn_interview": "🎤 Prepare for Interview",
        "btn_linkedin": "💼 Optimize My LinkedIn",
        "spinner_match": "🔍 AI is analyzing your match...",
        "spinner_resume": "✨ AI is tailoring your resume...",
        "spinner_cover": "📝 AI is writing your cover letter...",
        "spinner_interview": "🎯 AI is preparing your interview guide...",
        "spinner_linkedin": "💼 AI is optimizing your LinkedIn...",
        "desc_match": "Analyzes how well your resume matches the job and tells you whether to apply, what to emphasize, and what you're missing.",
        "desc_resume": "Rewrites your resume to perfectly target this specific job — adds missing keywords, reorders sections, and strengthens your bullet points.",
        "desc_cover": "Generates a personalized, human-sounding cover letter that maps your experience directly to what they need. Not generic AI slop.",
        "desc_interview": "Generates likely interview questions for this specific role, with suggested answers based on YOUR actual experience. Plus a \"Tell me about yourself\" script.",
        "desc_linkedin": "Generates an optimized LinkedIn headline and About section packed with keywords that recruiters actually search for.",
        "tone_label": "Cover letter tone",
        "footer_privacy": "**🔒 Your data stays private**",
        "footer_privacy_sub": "Nothing is stored. Your resume goes directly to the AI and back to you.",
        "footer_tip": "**💡 Pro tip**",
        "footer_tip_sub": "Run all 5 tools for the same job to get the complete picture before applying.",
        "footer_track": "**📈 Track your results**",
        "footer_track_sub": "Apply only when match score > 70%. Customize resume for EVERY job.",
    },
    "Español": {
        "hero_title": "🚀 AI Job Interview Booster",
        "hero_sub": "Pega tu currículum + una descripción de trabajo → obtén materiales personalizados en segundos",
        "resume_label": "#### 📄 Tu Currículum",
        "resume_placeholder": "Pega tu currículum aquí...\n\nIncluye: nombre, experiencia, habilidades, educación",
        "job_label": "#### 💼 Descripción del Trabajo",
        "job_placeholder": "Pega la descripción completa del puesto...\n\nIncluye: título, requisitos, responsabilidades",
        "company_label": "🏢 Nombre de la empresa (opcional — mejora la carta de presentación)",
        "company_placeholder": "ej., Google, Accenture, Banco Nacional",
        "warn_resume": "⚠️ Por favor pega tu currículum (al menos unas oraciones)",
        "warn_job": "⚠️ Por favor pega la descripción del trabajo (al menos unas oraciones)",
        "warn_key": "🔑 Por favor ingresa tu API key en la barra lateral",
        "tab_match": "🧠 Puntuación de Match",
        "tab_resume": "✍️ Optimizar CV",
        "tab_cover": "📄 Carta de Presentación",
        "tab_interview": "🎤 Prep. Entrevista",
        "tab_linkedin": "💼 Optimizar LinkedIn",
        "btn_match": "🧠 Analizar Mi Match",
        "btn_resume": "✍️ Optimizar Mi CV",
        "btn_cover": "📄 Generar Carta",
        "btn_interview": "🎤 Preparar Entrevista",
        "btn_linkedin": "💼 Optimizar Mi LinkedIn",
        "spinner_match": "🔍 La IA está analizando tu match...",
        "spinner_resume": "✨ La IA está optimizando tu CV...",
        "spinner_cover": "📝 La IA está escribiendo tu carta...",
        "spinner_interview": "🎯 La IA está preparando tu guía de entrevista...",
        "spinner_linkedin": "💼 La IA está optimizando tu LinkedIn...",
        "desc_match": "Analiza qué tan bien tu currículum coincide con el trabajo y te dice si debes aplicar, qué enfatizar y qué te falta.",
        "desc_resume": "Reescribe tu CV para que esté perfectamente dirigido a este trabajo — agrega palabras clave, reordena secciones y fortalece tus logros.",
        "desc_cover": "Genera una carta de presentación personalizada que conecta tu experiencia directamente con lo que necesitan. Nada genérico.",
        "desc_interview": "Genera preguntas probables de entrevista para este puesto, con respuestas sugeridas basadas en TU experiencia real. Incluye un guion de \"Háblame de ti\".",
        "desc_linkedin": "Genera un titular y sección Acerca de optimizados con palabras clave que los reclutadores realmente buscan.",
        "tone_label": "Tono de la carta",
        "footer_privacy": "**🔒 Tus datos son privados**",
        "footer_privacy_sub": "Nada se almacena. Tu CV va directo a la IA y regresa a ti.",
        "footer_tip": "**💡 Consejo**",
        "footer_tip_sub": "Usa las 5 herramientas para el mismo trabajo antes de aplicar.",
        "footer_track": "**📈 Sigue tus resultados**",
        "footer_track_sub": "Aplica solo cuando el match sea > 70%. Personaliza el CV para CADA trabajo.",
    },
}
t = T[lang]


# ─── Hero ──────────────────────────────────────────
st.markdown(f"""
<div class="hero">
    <h1>{t['hero_title']}</h1>
    <p>{t['hero_sub']}</p>
</div>
""", unsafe_allow_html=True)


# ─── Input section ─────────────────────────────────
col1, col2 = st.columns(2)

with col1:
    st.markdown(t["resume_label"])
    resume = st.text_area(
        "resume", height=250, placeholder=t["resume_placeholder"], label_visibility="collapsed",
    )

with col2:
    st.markdown(t["job_label"])
    job = st.text_area(
        "job", height=250, placeholder=t["job_placeholder"], label_visibility="collapsed",
    )

company = st.text_input(t["company_label"], placeholder=t["company_placeholder"])


# ─── Validation ────────────────────────────────────
def check_inputs():
    if not resume or len(resume.strip()) < 50:
        st.warning(t["warn_resume"])
        return False
    if not job or len(job.strip()) < 50:
        st.warning(t["warn_job"])
        return False
    import os
    if not os.getenv("OPENAI_API_KEY") and not os.getenv("ANTHROPIC_API_KEY"):
        if api_source != "Ollama (Free Local)":
            st.error(t["warn_key"])
            return False
    return True


# ─── Feature tabs ──────────────────────────────────
st.divider()

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    t["tab_match"], t["tab_resume"], t["tab_cover"], t["tab_interview"], t["tab_linkedin"],
])


# ─── Tab 1: Job Match ─────────────────────────────
with tab1:
    st.markdown(f'<div class="feature-card"><strong>{"What this does:" if lang == "English" else "Qué hace:"}</strong> {t["desc_match"]}</div>', unsafe_allow_html=True)
    
    if st.button(t["btn_match"], key="match_btn", use_container_width=True, type="primary"):
        if check_inputs():
            with st.spinner(t["spinner_match"]):
                from ai_engine import generate
                from prompts import job_match_prompt, get_system
                result = generate(job_match_prompt(resume, job, lang), system=get_system(lang), temperature=0.3)
            
            import re
            score_match = re.search(r'(\d{1,3})\s*/\s*100', result)
            if score_match:
                score = int(score_match.group(1))
                if score >= 80:
                    color, emoji = "#0F6E56", "🟢"
                elif score >= 60:
                    color, emoji = "#2E75B6", "🔵"
                else:
                    color, emoji = "#D85A30", "🟠"
                
                st.markdown(f"""
                <div class="score-box" style="background: linear-gradient(135deg, {color} 0%, {color}99 100%);">
                    <div class="number">{emoji} {score}/100</div>
                    <div class="label">{"Job Match Score" if lang == "English" else "Puntuación de Match"}</div>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown(result)
            st.download_button("📥 Download" if lang == "English" else "📥 Descargar", result,
                             file_name="job_match_analysis.txt", mime="text/plain")


# ─── Tab 2: Resume Optimizer ──────────────────────
with tab2:
    st.markdown(f'<div class="feature-card green"><strong>{"What this does:" if lang == "English" else "Qué hace:"}</strong> {t["desc_resume"]}</div>', unsafe_allow_html=True)
    
    if st.button(t["btn_resume"], key="resume_btn", use_container_width=True, type="primary"):
        if check_inputs():
            with st.spinner(t["spinner_resume"]):
                from ai_engine import generate
                from prompts import resume_optimizer_prompt, get_system
                result = generate(resume_optimizer_prompt(resume, job, lang), system=get_system(lang), temperature=0.5)
            
            st.markdown(f'<div class="result-header">{"✅ Your Optimized Resume" if lang == "English" else "✅ Tu CV Optimizado"}</div>', unsafe_allow_html=True)
            st.markdown(result)
            st.download_button("📥 Download" if lang == "English" else "📥 Descargar", result,
                             file_name="optimized_resume.txt", mime="text/plain")


# ─── Tab 3: Cover Letter ─────────────────────────
with tab3:
    st.markdown(f'<div class="feature-card orange"><strong>{"What this does:" if lang == "English" else "Qué hace:"}</strong> {t["desc_cover"]}</div>', unsafe_allow_html=True)
    
    if lang == "English":
        tone_options = ["Casual", "Conversational", "Professional", "Formal"]
    else:
        tone_options = ["Casual", "Conversacional", "Profesional", "Formal"]
    
    tone = st.select_slider(t["tone_label"], options=tone_options, value=tone_options[2])
    
    if st.button(t["btn_cover"], key="cover_btn", use_container_width=True, type="primary"):
        if check_inputs():
            with st.spinner(t["spinner_cover"]):
                from ai_engine import generate
                from prompts import cover_letter_prompt, get_system
                prompt = cover_letter_prompt(resume, job, company, lang)
                if tone not in ["Professional", "Profesional"]:
                    prompt += f"\n\nTone: {tone}"
                result = generate(prompt, system=get_system(lang), temperature=0.7)
            
            st.markdown(f'<div class="result-header">{"✅ Your Cover Letter" if lang == "English" else "✅ Tu Carta de Presentación"}</div>', unsafe_allow_html=True)
            st.markdown(result)
            
            words = len(result.split())
            st.caption(f"📏 {words} {'words' if lang == 'English' else 'palabras'}")
            
            col_a, col_b = st.columns(2)
            with col_a:
                st.download_button("📥 Download" if lang == "English" else "📥 Descargar", result,
                                 file_name="cover_letter.txt", mime="text/plain")
            with col_b:
                regen_label = "🔄 Regenerate" if lang == "English" else "🔄 Regenerar"
                if st.button(regen_label, key="regen_cover"):
                    with st.spinner("..." ):
                        result2 = generate(prompt, system=get_system(lang), temperature=0.9)
                    st.markdown(result2)


# ─── Tab 4: Interview Prep ───────────────────────
with tab4:
    st.markdown(f'<div class="feature-card purple"><strong>{"What this does:" if lang == "English" else "Qué hace:"}</strong> {t["desc_interview"]}</div>', unsafe_allow_html=True)
    
    if st.button(t["btn_interview"], key="interview_btn", use_container_width=True, type="primary"):
        if check_inputs():
            with st.spinner(t["spinner_interview"]):
                from ai_engine import generate
                from prompts import interview_prep_prompt, get_system
                result = generate(interview_prep_prompt(resume, job, lang), system=get_system(lang), temperature=0.5)
            
            st.markdown(f'<div class="result-header">{"✅ Your Interview Prep Guide" if lang == "English" else "✅ Tu Guía de Preparación"}</div>', unsafe_allow_html=True)
            st.markdown(result)
            st.download_button("📥 Download" if lang == "English" else "📥 Descargar", result,
                             file_name="interview_prep.txt", mime="text/plain")


# ─── Tab 5: LinkedIn Optimizer ───────────────────
with tab5:
    st.markdown(f'<div class="feature-card"><strong>{"What this does:" if lang == "English" else "Qué hace:"}</strong> {t["desc_linkedin"]}</div>', unsafe_allow_html=True)
    
    if st.button(t["btn_linkedin"], key="linkedin_btn", use_container_width=True, type="primary"):
        if check_inputs():
            with st.spinner(t["spinner_linkedin"]):
                from ai_engine import generate
                from prompts import linkedin_optimizer_prompt, get_system
                result = generate(linkedin_optimizer_prompt(resume, job, lang), system=get_system(lang), temperature=0.6)
            
            st.markdown(f'<div class="result-header">{"✅ Your LinkedIn Optimization" if lang == "English" else "✅ Tu LinkedIn Optimizado"}</div>', unsafe_allow_html=True)
            st.markdown(result)
            st.download_button("📥 Download" if lang == "English" else "📥 Descargar", result,
                             file_name="linkedin_optimization.txt", mime="text/plain")


# ─── Footer ───────────────────────────────────────
st.divider()
col_f1, col_f2, col_f3 = st.columns(3)
with col_f1:
    st.markdown(t["footer_privacy"])
    st.caption(t["footer_privacy_sub"])
with col_f2:
    st.markdown(t["footer_tip"])
    st.caption(t["footer_tip_sub"])
with col_f3:
    st.markdown(t["footer_track"])
    st.caption(t["footer_track_sub"])
