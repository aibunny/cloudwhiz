import streamlit as st
import lang as lg 


st.title("💬 Cloudwhiz")
st.markdown("## Chat with an AWS SOLUTIONS ARCHITECT ASISSTANT built by [aibunny](https://www.theaibunny.com/) ")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    
    st.session_state.messages.append({"role": "You", "content": prompt})
    st.chat_message("user").write(prompt)
    response = lg.get_reponse_from_query(prompt)
    msg = response
    st.session_state.messages.append({"role":"You", "content" :msg})
    st.chat_message("assistant").write(msg)