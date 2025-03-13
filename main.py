import streamlit as st
from utils import get_chat_response
from langchain.memory import ConversationBufferMemory

st.title("Similar deepseek")

with st.sidebar:
    api = st.text_input("请输入你的API",type="password")
    st.markdown("[获取deepseek API key](https://platform.deepseek.com/api_keys)")
    if st.button("重新开始"):
        st.session_state["memory"].clear()
        st.session_state["messages"] = [{"role": "ai", "content": "我是你的ai助手，需要什么帮助吗？"}]
        st.experimental_rerun()

if "memory" not in st.session_state:
    st.session_state["memory"] = ConversationBufferMemory(return_messages=True)
    st.session_state["messages"] = [{"role":"ai","content":"我是你的ai助手，需要什么帮助吗？"}]

for message in st.session_state["messages"]:
    st.chat_message(message["role"]).write(message["content"])

prompt = st.chat_input()
if prompt:
    if not api:
        st.info("请输入你的api")
        st.stop()
    st.session_state["messages"].append({"role":"human","content":prompt})
    st.chat_message("human").write(prompt)
    with st.spinner("ai正在思考，请稍后..."):
        response = get_chat_response(prompt,st.session_state["memory"],api)

    msg = {"role":"ai","content":response}
    st.session_state["messages"].append(msg)
    st.chat_message("ai").write(response)

