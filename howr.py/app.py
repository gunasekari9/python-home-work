import streamlit as st
from new import chatbot

st.title("My Chatbot")

# keep the messages shown on the page
if "messages" not in st.session_state:
    st.session_state.messages = []

# show old messages like a chat
for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.write(m["content"])

# input box at the bottom
prompt = st.chat_input("Type a message...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            answer = chatbot(prompt)
        st.write(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})