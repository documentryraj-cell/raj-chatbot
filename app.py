import streamlit as st
from groq import Groq

# Page Settings
st.set_page_config(page_title="raj AI chatbot", page_icon="🤖")
st.title("Welcome to Raj Chatbot")

# Client initialization (Groq ke liye)
if "client" not in st.session_state:
    st.session_state.client = Groq(api_key="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")
# Messages Display aur Input
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Raj se kuch puchiye..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        # Llama 3 model use kar rahe hain jo bohot fast hai
        response = st.session_state.client.chat.completions.create(
            messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
            model="llama-3.3-70b-versatile",
        )
        output = response.choices[0].message.content
        with st.chat_message("assistant"):
            st.markdown(output)
        st.session_state.messages.append({"role": "assistant", "content": output})
    except Exception as e:
        st.error(f"Error: {e}")