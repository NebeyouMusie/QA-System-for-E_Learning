import streamlit as st
from langchain_utils import get_qa_chain, create_vector_db

st.title('E-learning Q&A ❓')

btn = st.button('Create Knowledgebase')

if btn:
    create_vector_db()

question = st.text_input('Question: ')

if question:
    chain = get_qa_chain()
    response = chain.invoke(question)

    st.header('Answer')
    st.write(response['result'])