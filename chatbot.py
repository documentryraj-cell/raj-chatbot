import os
import streamlit as st
from google import genai

# Page Settings
st.set_page_config(page_title="Raj AI Bot", page_icon="🤖")
st.title("Welcome to Raj Chatbot")

# Gemini API Key
os.environ["GEMINI_API_KEY"] = "AQ.Ab8RN6JKw-vMy1FTyDsYfSiTSSyCNy9WVyJNkDftTdaiNkCbIA"

if "client" not in st.session_state:
    st.session_state.client = genai.Client()

# Chat Session
if "chat_session" not in st.session_state:
    st.session_state.chat_session = st.session_state.client.chats.create(
        model="gemini-2.5-flash",
        config={
            "system_instruction": "Raj ek friendly AI assistant hai jo Hinglish mein jawab deta hai."
        }
    )

# Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Old Messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["text"])

# User Input
if user_input := st.chat_input("Raj se kuch puchiye..."):

    with st.chat_message("user"):
        st.markdown(user_input)

    st.session_state.messages.append({
        "role": "user",
        "text": user_input
    })

    try:
        with st.spinner("Raj is thinking..."):
            response = st.session_state.chat_session.send_message(user_input)

        with st.chat_message("assistant"):
            st.markdown(response.text)

        st.session_state.messages.append({
            "role": "assistant",
            "text": response.text
        })

    except Exception as e:
        st.error(f"Error: {e}")