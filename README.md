# 🙌 AI-TRAVEL-AGENT

Welcome to **AI-Travel-Agent** — an offline, **ultra-fast AI travel planner** built using **Ollama, Agno & Streamlit**.  
This project runs completely on your own laptop (no API costs!), generates detailed travel answers in seconds, and is perfect for **demonstrations, portfolio work, and real-world usage**!

---

## 🚀 🔥 Project Overview

AI-Travel-Agent is a **local AI travel assistant** that answers complex travel questions instantly.  
Example: Query like _“Plan a 2-person trip: 3 days in Turkey then 15 days in Saudi Arabia”_ will return:  
✔ Day-by-day itinerary  
✔ Flight suggestions  
✔ Hotel plans  
✔ Budget estimates  
✔ Food & activity recommendations  

All of this is generated **offline** using an open-source LLM model — no cloud APIs needed. :contentReference[oaicite:0]{index=0}

---

## 🛠️ 🧠 Tech Stack

| Component | Technology |
|-----------|------------|
| UI | Streamlit |
| AI Logic | Agno Agent Framework |
| LLM Backend | Ollama (local models) |
| Model Used | `qwen2.5:0.5b` — fast & lightweight |

---

## 📦 📁 Project Structure
AI-TRAVEL-AGENT/
├── agent.py
├── app.py
├── requirements.txt
├── static/
│ └── style.css
└── README.md


---

## ✨ ⭐ Features

✔ Works 100% offline  
✔ Zero API costs  
✔ Fast response travel answers  
✔ Styled UI with Streamlit  
✔ Modular Agent backend using Agno  
✔ Easy to extend & deploy  
✔ Perfect for portfolio showcase

---

## 🔧 Installation Guide

### 1️⃣ Clone the repository
```bash
git clone https://github.com/HassanShahidDev/AI-TRAVEL-AGENT.git
cd AI-TRAVEL-AGENT

2️⃣ Set up Python environment
python -m venv .venv
.venv\Scripts\activate     # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

🧠 Setup Ollama Models

This project requires a small model for speed and performance.

⚡ Install the fastest model:
ollama pull qwen2.5:0.5b

🧠 Run Ollama server
ollama serve

▶️ Run the App
streamlit run app.py


Open in browser:

http://localhost:8501

🧩 Code Snippets & Explanation
🧠 agent.py
from agno.agent import Agent
from agno.models.ollama import Ollama

travel_agent = Agent(
    model=Ollama(id="qwen2.5:0.5b"),
    description="Fast offline travel assistant",
)


✔ Defines an AI agent
✔ Uses Ollama local model
✔ Fast & offline inference

📱 app.py (Streamlit)
import streamlit as st
from agent import travel_agent

st.set_page_config(
    page_title="Travel AI Agent",
    page_icon="✈️",
    layout="wide"
)

with open("static/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("✈️ Travel AI Agent — Your Travel Companion")
st.markdown("""
<p style='text-align: center; color:#ddd; font-size:18px;'>
Powered by <strong>Ollama + Streamlit + Agno</strong>
</p>
""", unsafe_allow_html=True)

question = st.text_input("Ask any travel question:")

if st.button("Ask"):
    if question.strip() == "":
        st.warning("Please type a question.")
    else:
        with st.spinner("Thinking..."):
            answer = travel_agent.run(question)
        st.success("Answer Ready:")
        st.write(answer.content)


✔ Custom CSS for theme
✔ Input box + button
✔ AI answer output area

🎨 Custom Styling
static/style.css
body {
  background-color: #0f172a;
}

.stApp {
  background: linear-gradient(135deg, #041b3d, #092c57);
  color: white;
}


✔ Dark stylish background
✔ Clean UI for travel questions

📄 Usage Example

Ask something like:

Plan a trip for 2 people:
3 days in Turkey,
then 15 days in Saudi Arabia.
Include itinerary + hotels + flights + budget.


Project returns a complete travel plan 🧭🔥

💡 What Makes This Unique?

⭐ Runs locally — No API costs
⭐ Lightweight model — super fast responses
⭐ Easy code — beginner-friendly + scalable
⭐ Good for portfolio & resume

📌 Future Improvements
Feature	Status
Chat history	🟡 Planned
Export PDF/Doc	🟡 Planned
Voice input	🔴 Not Started
Deploy-to-Web	🟢 Possible
📣 Credits

Made by HassanShahidDev
Email: hassanshahid778866@gmail.com

