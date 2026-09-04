# AI Chatbot

A conversational AI web app built with Python and the Groq API, deployed live on Streamlit Cloud.

🔗 **Live Demo:** https://aichatbot-s4xlmx5wzjtlgc4b6eg63a.streamlit.app/

## Features
- Real-time conversational AI powered by an LLM (via Groq API)
- Maintains conversation memory within a session
- Custom AI personality via system prompting
- Simple, clean chat interface built with Streamlit
- Deployed publicly with secure API key handling

## Tech Stack
- Python
- Groq API (LLM inference)
- Streamlit (web app framework)
- Git & GitHub (version control)
- Streamlit Cloud (deployment)

## What I Learned
- Working with LLM APIs and prompt engineering
- Managing conversation state/memory in a chat application
- Securely handling API keys using environment secrets
- Deploying a Python app to a public cloud platform
- Using Git/GitHub for version control

## Run It Locally
git clone https://github.com/fathimaahsana17-collab/ai_chatbot.git
cd ai_chatbot
pip install -r requirements.txt
streamlit run chatbot.py

You'll need your own Groq API key in a `.streamlit/secrets.toml` file:
```toml
GROQ_API_KEY = "your-key-here"
```