from __future__ import annotations
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain

def get_chat_response(prompt,memory,api):
    model = ChatOpenAI(model="deepseek-chat",
                       api_key=api,
                       base_url="https://api.deepseek.com",
                       )
    chain = ConversationChain(llm=model,memory=memory)
    response = chain.invoke({"input" : prompt})
    return response["response"]