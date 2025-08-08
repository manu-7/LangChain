import streamlit as st
import requests

st.title("🧠 Question-Answering Bot (Phi)")

question = st.text_input("Enter your question:")

if question:
    try:
        response = requests.post(
            "http://localhost:8000/ask",
            json={"question": question},
            timeout=30
        )
        data = response.json()
        st.markdown(f"**Answer:** {data['answer']}")
    except Exception as e:
        st.error(f"Error: {e}")
