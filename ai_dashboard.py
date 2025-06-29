import streamlit as st
import requests

# --- Page Setup ---
st.set_page_config(page_title="Sharad's AI Hub", page_icon="🧠", layout="wide")

# --- Custom Static Styling ---
st.markdown("""
<style>
.stApp {
  background: linear-gradient(145deg, #1a1f2b, #2c3e50, #34495e, #1b2735);
  font-family: 'Segoe UI', sans-serif;
  color: white;
  padding-bottom: 40px;
}

h1 {
  font-size: 2.8em;
  text-align: center;
  margin-bottom: 0.25rem;
}

.subtitle {
  font-size: 0.85em;
  text-align: center;
  color: #cccccc;
  margin-top: 0;
}

.app-box {
  background-color: #00b8d4;
  color: black;
  padding: 20px;
  border-radius: 10px;
  font-size: 1.3em;
  text-align: center;
  font-weight: bold;
  box-shadow: 0 0 12px rgba(0, 184, 212, 0.4);
  transition: background-color 0.3s, box-shadow 0.3s;
  width: 275px;
  margin: 15px auto;
}

.app-box:hover {
  background-color: #00acc1;
  box-shadow: 0 0 16px rgba(0, 184, 212, 0.7);
}

a {
  text-decoration: none;
  color: black;
}

.status {
  font-size: 0.8em;
  color: #666;
  margin-top: 6px;
  font-weight: normal;
}
</style>
""", unsafe_allow_html=True)

# --- Title & Subtitle ---
st.markdown("<h1>🚀 Welcome to Drive Tech's AI Hub</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Explore my growing toolkit of intelligent applications</p>", unsafe_allow_html=True)

# --- App List ---
apps = {
    "🤖 Q&A Chatbot": "https://qa-chatbot.drive-tech-ai.com",
    "🧠 Essay Writer": "https://qa.sharad.ai",
    "📊 PDF Analyser": "https://data.sharad.ai"
}

def check_status(url):
    try:
        requests.get(url, timeout=1)
        return "✅ Online"
    except:
        return "❌ Offline"

# --- App Grid (3 Columns) ---
cols = st.columns(3)
for col, (name, url) in zip(cols, apps.items()):
    with col:
        status = check_status(url)
        st.markdown(f"""
            <div class="app-box">
                <a href="{url}" target="_blank">{name}</a>
                <div class="status">{status}</div>
            </div>
        """, unsafe_allow_html=True)

# --- Footer ---
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:#aaaaaa;font-size:0.85em;'>Made with ❤️ by Drive Tech AI • sharad@drive-tech-ai.com</p>", unsafe_allow_html=True)
