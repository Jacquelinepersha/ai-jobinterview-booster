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
        st.info("Make sure Ollama is running locally")
        import os
        os.environ.pop("OPENAI_API_KEY", None)
        os.environ.pop("ANTHROPIC_API_KEY", None)
    
    st.divider()
    st.markdown("### 📊 How to use")
    st.markdown("""
    1. **Paste** your resume below
    2. **Paste** a job description
    3. **Pick** a tool from the tabs
    4. **Click** the button — done!
    
    💡 *Each result is tailored to that specific job*
    """)
    
    st.divider()
    st.markdown("### 💰 Cost per use")
    st.markdown("""
    | Action | Cost |
    |--------|------|
    | Job Match | ~$0.01 |
    | Resume Optimize | ~$0.02 |
    | Cover Letter | ~$0.01 |
    | Interview Prep | ~$0.01 |
    | LinkedIn Optimize | ~$0.01 |
    """)
    st.caption("Prices based on GPT-4o-mini. Claude may vary slightly.")


# ─── Hero ──────────────────────────────────────────
st.markdown("""
<div class="hero">
    <h1>🚀 AI Job Interview Booster</h1>
    <p>Paste your resume + a job description → get tailored materials in seconds</p>
</div>
""", unsafe_allow_html=True)


# ─── Input section ─────────────────────────────────
col1, col2 = st.columns(2)

with col1:
    st.markdown("#### 📄 Your Resume")
    resume = st.text_area(
        "Paste your full resume here",
        height=250,
        placeholder="Paste your resume text here...\n\nInclude: name, experience, skills, education",
        label_visibility="collapsed",
    )

with col2:
    st.markdown("#### 💼 Job Description")
    job = st.text_area(
        "Paste the job description here",
        height=250,
        placeholder="Paste the full job posting here...\n\nInclude: title, requirements, responsibilities",
        label_visibility="collapsed",
    )

# Optional company name
company = st.text_input("🏢 Company name (optional — improves cover letter personalization)", placeholder="e.g., Stripe, Google, Acme Corp")


# ─── Validation ────────────────────────────────────
def check_inputs():
    if not resume or len(resume.strip()) < 50:
        st.warning("⚠️ Please paste your resume (at least a few sentences)")
        return False
    if not job or len(job.strip()) < 50:
        st.warning("⚠️ Please paste the job description (at least a few sentences)")
        return False
    # Check API key
    import os
    if not os.getenv("OPENAI_API_KEY") and not os.getenv("ANTHROPIC_API_KEY"):
        if api_source != "Ollama (Free Local)":
            st.error("🔑 Please enter your API key in the sidebar")
            return False
    return True


# ─── Feature tabs ──────────────────────────────────
st.divider()

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🧠 Job Match Score",
    "✍️ Optimize Resume",
    "📄 Cover Letter",
    "🎤 Interview Prep",
    "💼 LinkedIn Optimizer",
])


# ─── Tab 1: Job Match ─────────────────────────────
with tab1:
    st.markdown("""
    <div class="feature-card">
        <strong>What this does:</strong> Analyzes how well your resume matches the job and tells you 
        whether to apply, what to emphasize, and what you're missing.
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🧠 Analyze My Match", key="match_btn", use_container_width=True, type="primary"):
        if check_inputs():
            with st.spinner("🔍 AI is analyzing your match..."):
                from ai_engine import generate
                from prompts import job_match_prompt, SYSTEM
                result = generate(job_match_prompt(resume, job), system=SYSTEM, temperature=0.3)
            
            # Try to extract score for the big display
            import re
            score_match = re.search(r'(\d{1,3})\s*/\s*100', result)
            if score_match:
                score = int(score_match.group(1))
                # Color based on score
                if score >= 80:
                    color = "#0F6E56"
                    emoji = "🟢"
                elif score >= 60:
                    color = "#2E75B6"
                    emoji = "🔵"
                else:
                    color = "#D85A30"
                    emoji = "🟠"
                
                st.markdown(f"""
                <div class="score-box" style="background: linear-gradient(135deg, {color} 0%, {color}99 100%);">
                    <div class="number">{emoji} {score}/100</div>
                    <div class="label">Job Match Score</div>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown(result)
            
            # Download button
            st.download_button(
                "📥 Download Analysis",
                result,
                file_name="job_match_analysis.txt",
                mime="text/plain",
            )


# ─── Tab 2: Resume Optimizer ──────────────────────
with tab2:
    st.markdown("""
    <div class="feature-card green">
        <strong>What this does:</strong> Rewrites your resume to perfectly target this specific job — 
        adds missing keywords, reorders sections, and strengthens your bullet points.
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("✍️ Optimize My Resume", key="resume_btn", use_container_width=True, type="primary"):
        if check_inputs():
            with st.spinner("✨ AI is tailoring your resume..."):
                from ai_engine import generate
                from prompts import resume_optimizer_prompt, SYSTEM
                result = generate(resume_optimizer_prompt(resume, job), system=SYSTEM, temperature=0.5)
            
            st.markdown('<div class="result-header">✅ Your Optimized Resume</div>', unsafe_allow_html=True)
            st.markdown(result)
            
            st.download_button(
                "📥 Download Optimized Resume",
                result,
                file_name="optimized_resume.txt",
                mime="text/plain",
            )


# ─── Tab 3: Cover Letter ─────────────────────────
with tab3:
    st.markdown("""
    <div class="feature-card orange">
        <strong>What this does:</strong> Generates a personalized, human-sounding cover letter that 
        maps your experience directly to what they need. Not generic AI slop.
    </div>
    """, unsafe_allow_html=True)
    
    tone = st.select_slider(
        "Cover letter tone",
        options=["Casual", "Conversational", "Professional", "Formal"],
        value="Professional",
    )
    
    if st.button("📄 Generate Cover Letter", key="cover_btn", use_container_width=True, type="primary"):
        if check_inputs():
            with st.spinner("📝 AI is writing your cover letter..."):
                from ai_engine import generate
                from prompts import cover_letter_prompt, SYSTEM
                prompt = cover_letter_prompt(resume, job, company)
                if tone != "Professional":
                    prompt += f"\n\nTone: {tone}"
                result = generate(prompt, system=SYSTEM, temperature=0.7)
            
            st.markdown('<div class="result-header">✅ Your Cover Letter</div>', unsafe_allow_html=True)
            st.markdown(result)
            
            # Word count
            words = len(result.split())
            st.caption(f"📏 {words} words")
            
            col_a, col_b = st.columns(2)
            with col_a:
                st.download_button(
                    "📥 Download as Text",
                    result,
                    file_name="cover_letter.txt",
                    mime="text/plain",
                )
            with col_b:
                if st.button("🔄 Regenerate (different version)", key="regen_cover"):
                    with st.spinner("Writing another version..."):
                        result2 = generate(prompt, system=SYSTEM, temperature=0.9)
                    st.markdown(result2)


# ─── Tab 4: Interview Prep ───────────────────────
with tab4:
    st.markdown("""
    <div class="feature-card purple">
        <strong>What this does:</strong> Generates likely interview questions for this specific role, 
        with suggested answers based on YOUR actual experience. Plus a "Tell me about yourself" script.
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🎤 Prepare for Interview", key="interview_btn", use_container_width=True, type="primary"):
        if check_inputs():
            with st.spinner("🎯 AI is preparing your interview guide..."):
                from ai_engine import generate
                from prompts import interview_prep_prompt, SYSTEM
                result = generate(interview_prep_prompt(resume, job), system=SYSTEM, temperature=0.5)
            
            st.markdown('<div class="result-header">✅ Your Interview Prep Guide</div>', unsafe_allow_html=True)
            st.markdown(result)
            
            st.download_button(
                "📥 Download Interview Prep",
                result,
                file_name="interview_prep.txt",
                mime="text/plain",
            )


# ─── Tab 5: LinkedIn Optimizer ───────────────────
with tab5:
    st.markdown("""
    <div class="feature-card">
        <strong>What this does:</strong> Generates an optimized LinkedIn headline and About section 
        packed with keywords that recruiters actually search for.
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("💼 Optimize My LinkedIn", key="linkedin_btn", use_container_width=True, type="primary"):
        if check_inputs():
            with st.spinner("💼 AI is optimizing your LinkedIn..."):
                from ai_engine import generate
                from prompts import linkedin_optimizer_prompt, SYSTEM
                result = generate(linkedin_optimizer_prompt(resume, job), system=SYSTEM, temperature=0.6)
            
            st.markdown('<div class="result-header">✅ Your LinkedIn Optimization</div>', unsafe_allow_html=True)
            st.markdown(result)
            
            st.download_button(
                "📥 Download LinkedIn Copy",
                result,
                file_name="linkedin_optimization.txt",
                mime="text/plain",
            )


# ─── Footer ───────────────────────────────────────
st.divider()
col_f1, col_f2, col_f3 = st.columns(3)
with col_f1:
    st.markdown("**🔒 Your data stays private**")
    st.caption("Nothing is stored. Your resume goes directly to the AI and back to you.")
with col_f2:
    st.markdown("**💡 Pro tip**")
    st.caption("Run all 5 tools for the same job to get the complete picture before applying.")
with col_f3:
    st.markdown("**📈 Track your results**")
    st.caption("Apply only when match score > 70%. Customize resume for EVERY job.")
