import streamlit as st
import requests

st.set_page_config(page_title="Sharad's AI App Hub", page_icon="🧠" )
st.title("🧠 Sharad's AI App Dashboard")
st.write("Monitor and launch your AI projects:")

apps = {
    "Chatbot": "https://qa-chatbot.drive-tech-ai.com/",
    "Q&A Assistant": "https://qa.sharad.ai",
    "Data Explorer": "https://data.sharad.ai"
}

def check_status(url):
    try:
        r = requests.get(url, timeout=1)
        return "✅ Online"
    except:
        return "❌ Offline"

for name, url in apps.items():
    col1, col2 = st.columns([2, 1])
    col1.markdown(f"**{name}** — {check_status(url)}")
    col2.markdown(f"[Launch]({url})", unsafe_allow_html=True)
