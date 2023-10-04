from backend.core import run_llm
import streamlit as st
from streamlit_chat import message
from typing import Set


def create_sources_string(sources_urls: Set[str]) -> str:
    if not sources_urls:
        return ""
    sources_list = list(sources_urls)
    sources_list.sort()
    sources_string = "sources:\n"
    for i, source in enumerate(sources_list):
        sources_string += f"{i+1}. {source}\n"
    return sources_string


st.header("Langchain Documentation Helper Bot")

prompt = st.text_input("Prompt", placeholder="What are you looking for?")

if "user_prompt_history" not in st.session_state:
    st.session_state["user_prompt_history"] = []

if "chat_answers_history" not in st.session_state:
    st.session_state["chat_answers_history"] = []

if prompt:
    with st.spinner("Looking for useful information"):
        response = run_llm(prompt)
        sources = set([doc.metadata["source"] for doc in response["source_documents"]])

        result = response["result"]
        formatted_response = f"{result} \n\n {create_sources_string(sources)}"

        st.session_state["user_prompt_history"].append(prompt)
        st.session_state["chat_answers_history"].append(formatted_response)

if st.session_state["chat_answers_history"]:
    for response, query in zip(
        st.session_state["chat_answers_history"],
        st.session_state["user_prompt_history"]
    ):
        message(query, is_user=True)
        message(response)
