import streamlit as st
from groq import Groq

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

st.title("🤖 My AI Chatbot")

if "conversation" not in st.session_state:
    st.session_state.conversation = []

# Show past messages
for msg in st.session_state.conversation:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Get new input
user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.conversation.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[{"role": "system", "content": "You are a friendly, encouraging coding tutor who explains things simply."}] + st.session_state.conversation
    )

    reply = response.choices[0].message.content
    st.session_state.conversation.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.write(reply)