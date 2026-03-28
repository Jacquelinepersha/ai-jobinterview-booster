"""
AI Engine — multi-provider LLM wrapper.
Supports OpenAI, Anthropic Claude, and Ollama (free local).
Auto-detects which API key is available and uses it.
"""
import os
import json
from dotenv import load_dotenv

load_dotenv()


def _get_provider():
    """Auto-detect which provider to use based on available keys."""
    if os.getenv("ANTHROPIC_API_KEY"):
        return "anthropic"
    if os.getenv("OPENAI_API_KEY"):
        return "openai"
    # Only try Ollama if running locally (not on Streamlit Cloud)
    if os.getenv("OLLAMA_URL"):
        return "ollama"
    return None


def generate(prompt: str, system: str = "", temperature: float = 0.7, max_tokens: int = 2500) -> str:
    """Generate text using whichever AI provider is configured."""
    provider = _get_provider()

    if provider is None:
        raise ConnectionError(
            "No API key found. Please enter your OpenAI or Anthropic API key "
            "in the sidebar on the left. You can get a key at:\n\n"
            "• OpenAI: https://platform.openai.com/api-keys\n"
            "• Anthropic: https://console.anthropic.com\n\n"
            "Keys are NOT stored — they stay in your browser session only."
        )

    if provider == "anthropic":
        return _call_anthropic(prompt, system, temperature, max_tokens)
    elif provider == "openai":
        return _call_openai(prompt, system, temperature, max_tokens)
    else:
        return _call_ollama(prompt, system, temperature, max_tokens)


def _call_anthropic(prompt, system, temperature, max_tokens):
    from anthropic import Anthropic
    client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    kwargs = {
        "model": os.getenv("MODEL", "claude-sonnet-4-20250514"),
        "max_tokens": max_tokens,
        "temperature": temperature,
        "messages": [{"role": "user", "content": prompt}],
    }
    if system:
        kwargs["system"] = system
    response = client.messages.create(**kwargs)
    return response.content[0].text


def _call_openai(prompt, system, temperature, max_tokens):
    from openai import OpenAI
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})
    response = client.chat.completions.create(
        model=os.getenv("MODEL", "gpt-4o-mini"),
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return response.choices[0].message.content


def _call_ollama(prompt, system, temperature, max_tokens):
    import requests
    base = os.getenv("OLLAMA_URL", "http://localhost:11434")
    payload = {
        "model": os.getenv("MODEL", "llama3"),
        "prompt": prompt,
        "stream": False,
        "options": {"temperature": temperature, "num_predict": max_tokens},
    }
    if system:
        payload["system"] = system
    try:
        resp = requests.post(f"{base}/api/generate", json=payload, timeout=120)
        resp.raise_for_status()
        return resp.json()["response"]
    except requests.exceptions.ConnectionError:
        raise ConnectionError(
            "Could not connect to Ollama. If you're using Streamlit Cloud, "
            "Ollama won't work — please enter an OpenAI or Anthropic API key "
            "in the sidebar instead."
        )


def get_provider_name() -> str:
    """Return friendly name of active provider."""
    p = _get_provider()
    if p is None:
        return "No provider configured"
    names = {"anthropic": "Claude (Anthropic)", "openai": "GPT-4o (OpenAI)", "ollama": "Local AI (Ollama)"}
    return names.get(p, p)
