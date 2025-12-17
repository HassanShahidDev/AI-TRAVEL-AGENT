import streamlit as st
from agent import travel_agent

st.set_page_config(page_title="Travel AI Agent", page_icon="✈️", layout="wide")

with open("static/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("✈️ Travel AI Agent — Your Travel Companion")

st.markdown("""
<p style='text-align: center; font-size:18px; color:#d1d5db;'>
Powered by <strong>Ollama + Streamlit + Agno</strong> — fast, offline & intelligent travel planning
</p>
""", unsafe_allow_html=True)

st.write("Ask any travel question...")


question = st.text_input("Enter your question:")

if st.button("Ask"):
    if question.strip() == "":
        st.warning("Please type a question.")
    else:
        with st.spinner("Thinking..."):
            answer = travel_agent.run(question)
        st.success("Answer Ready:")
        st.write(answer.content)
