<p align="center">
  <h1 align="center">🚀 AI Job Interview Booster</h1>
  <p align="center">
    Paste your resume + a job description → get tailored materials in seconds
    <br />
    <strong>5 AI tools · 1 simple app · ~6 cents per job application</strong>
  </p>
</p>

<p align="center">
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License: MIT"></a>
  <a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/Python-3.10+-green.svg" alt="Python 3.10+"></a>
  <a href="https://streamlit.io/"><img src="https://img.shields.io/badge/Built%20with-Streamlit-FF4B4B.svg" alt="Built with Streamlit"></a>
  <a href="#"><img src="https://img.shields.io/badge/AI-OpenAI%20%7C%20Claude%20%7C%20Ollama-purple.svg" alt="AI Providers"></a>
</p>

---

## What it does

| Tool | What you get |
|------|-------------|
| 🧠 **Job Match Score** | Match % (0-100) + strengths + missing skills + red flags + should you apply? |
| ✍️ **Resume Optimizer** | Your resume rewritten with job-specific keywords + what changed and why |
| 📄 **Cover Letter** | Personalized, human-sounding letter with adjustable tone |
| 🎤 **Interview Prep** | Likely questions + suggested answers + "tell me about yourself" script |
| 💼 **LinkedIn Optimizer** | Optimized headline + About section + recruiter search keywords |

> **Why not just use ChatGPT?** You could — but you'd need to write a perfect prompt every time. This app uses carefully engineered prompts tested to produce the best output consistently. You just paste and click.

---

## Quick Start

### Option 1: Run locally (3 minutes)

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/ai-job-interview-booster.git
cd ai-job-interview-booster

# Install dependencies
pip install -r requirements.txt

# Add your API key
cp .env.example .env
# Edit .env and paste your OpenAI or Anthropic key

# Launch
streamlit run app.py
```

Opens in your browser at `http://localhost:8501`

### Option 2: Deploy to Streamlit Cloud (free, 2 minutes)

1. Fork this repo
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Click **"New app"** → select your forked repo → pick `app.py`
4. Add your API key in **Settings → Secrets**:
   ```toml
   OPENAI_API_KEY = "sk-..."
   ```
5. Click **Deploy** — done!

> 💡 **Users can also enter their own API key in the sidebar**, so you don't need to pay for their usage.

---

## How to get an API key

You need **one** of these (pick whichever you prefer):

| Provider | Best for | Cost | Get key |
|----------|---------|------|---------|
| **OpenAI** | Easiest setup | ~$0.01-0.02/use | [platform.openai.com/api-keys](https://platform.openai.com/api-keys) |
| **Anthropic Claude** | Best quality | ~$0.01-0.03/use | [console.anthropic.com](https://console.anthropic.com) |
| **Ollama** (local) | 100% free | $0 | [ollama.ai](https://ollama.ai) → `ollama pull llama3` |

---

## How to use it

1. **Paste** your full resume in the left box
2. **Paste** the job description in the right box
3. **Click** "Job Match Score" first — if it's below 70, skip this job
4. **If 70+**: run Resume Optimizer + Cover Letter
5. **Download** the results and apply
6. **Before interviews**: run Interview Prep

### The strategy that gets interviews

```
Find 5-10 jobs → Score them → Apply only to 70+ matches → Customize everything
```

This beats sending 100 generic applications. Quality over quantity.

---

## Cost per use

| Tool | Cost |
|------|------|
| Job Match Score | ~$0.01 |
| Resume Optimizer | ~$0.02 |
| Cover Letter | ~$0.01 |
| Interview Prep | ~$0.01 |
| LinkedIn Optimizer | ~$0.01 |
| **Full application** | **~$0.06** |

That's six cents per tailored application. A serious job search costs about $4/week.

---

## Project structure

```
ai-job-interview-booster/
├── app.py              ← Streamlit web interface (tabs, inputs, results)
├── ai_engine.py        ← Multi-provider AI wrapper (OpenAI / Claude / Ollama)
├── prompts.py          ← Engineered prompts for each tool
├── requirements.txt    ← Python dependencies
├── .env.example        ← API key template
├── .gitignore
├── .streamlit/
│   └── config.toml     ← Theme and server settings
├── LICENSE             ← MIT — use it however you want
└── README.md           ← You're reading it
```

---

## Features

- **Multi-provider AI**: Works with OpenAI, Anthropic Claude, or free local models via Ollama. Auto-detects which is available.
- **Per-job tailoring**: Every output is customized for the specific job description you paste in.
- **Download everything**: Every result has a download button — save and use directly.
- **Tone control**: Adjust cover letter tone from casual to formal.
- **Regenerate**: Don't like the cover letter? Click regenerate for a different version.
- **Privacy first**: Nothing is stored. Your resume goes to the AI and back to you. That's it.
- **No account needed**: Run it locally, no signup required.

---

## Honest expectations

**This tool WILL:**
- Make your resume significantly stronger for each specific job
- Save you 30-60 minutes per application
- Help you identify which jobs are worth applying to
- Give you a competitive edge in application screening

**This tool will NOT:**
- Guarantee interviews (no tool can — anyone who says otherwise is lying)
- Replace networking (referrals are still #1)
- Bypass competition (but it puts you in the top 10% of applicants)

---

## Contributing

Contributions are welcome! Here's how:

1. Fork the repo
2. Create a feature branch: `git checkout -b feature/my-feature`
3. Make your changes
4. Test locally: `streamlit run app.py`
5. Commit: `git commit -m "Add my feature"`
6. Push: `git push origin feature/my-feature`
7. Open a Pull Request

### Ideas for contributions
- [ ] PDF resume upload (parse and extract text)
- [ ] Save history of analyses
- [ ] Side-by-side resume comparison (before/after)
- [ ] Email follow-up generator
- [ ] Salary negotiation advisor
- [ ] Support for more languages
- [ ] Dark mode improvements

---

## FAQ

<details>
<summary><b>Can I use this commercially?</b></summary>
Yes. MIT license — use it, modify it, sell it, build a business with it.
</details>

<details>
<summary><b>Is my data safe?</b></summary>
Your resume is sent to the AI provider you choose (OpenAI/Anthropic) and back to you. Nothing is stored on any server. If you use Ollama, everything stays on your machine.
</details>

<details>
<summary><b>Why not just use ChatGPT directly?</b></summary>
You could! But you'd need to write a detailed prompt each time and the output format would vary. This app uses carefully engineered prompts that produce structured, consistent results every time. Paste, click, done.
</details>

<details>
<summary><b>"pip" or "streamlit" not found?</b></summary>
Try <code>pip3</code> instead of <code>pip</code>, or <code>python -m streamlit run app.py</code>. On Windows, try <code>py -m pip install -r requirements.txt</code>.
</details>

<details>
<summary><b>Can I deploy this for my team/company?</b></summary>
Yes. Deploy on Streamlit Cloud (free) or any server that runs Python. For private use, add authentication via Streamlit's built-in auth or deploy behind a VPN.
</details>

---

## Star History

If this tool helped your job search, give it a ⭐! It helps others find it.

---

## License

MIT — free to use, modify, and distribute.

---

Built by [Jacquie Persha](https://x.com/jacquiepersha) · Co-founder of [NextGenIQ.io](https://nextgeniq.io), the AI visibility platform for B2B brands.

<p align="center">
  <strong>Built with ❤️ to make content creation 10x faster</strong>
  <br />
  <sub>Record once, repurpose everywhere.</sub>
</p>
