from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAI
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_community.embeddings import HuggingFaceInstructEmbeddings
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
import os

from dotenv import load_dotenv

load_dotenv() # take environment variables from .env

# get google api key from .env
api_key = os.environ['GOOGLE_API_KEY']

# Create GoogleGenerativeAI LLM model
llm = GoogleGenerativeAI(model='gemini-pro', google_api_key=api_key)

# Initialize instructor embeddings using the hugging face model
instructor_embeddings = HuggingFaceInstructEmbeddings()
vector_file_path = 'faiss_index'

# function to create vector database
def create_vector_db():
    # Load data from csv sheet
    loader = CSVLoader(file_path='QA-System-for-E_Learning/codebasics_faqs.csv', source_column='prompt', encoding='latin')
    data = loader.load()

    # create a FAISS instance for vector from 'data'
    vectordb = FAISS.from_documents(documents=data, embedding=instructor_embeddings)

    # Save vector database locally
    vectordb.save_local('QA-System-for-E_Learning/' + vector_file_path) 

# function to get Q & A chain
def get_qa_chain():
    # Load the vector database from the local folder
    vectordb = FAISS.load_local('QA-System-for-E_Learning/' + vector_file_path, instructor_embeddings, allow_dangerous_deserialization=True)

    # Create a retriever for querying teh vector database
    retriever = vectordb.as_retriever(score_threshold=0.7)

    # Create the prompt template
    prompt_template = """Given the following context and a question, generate an answer based on this context only.
    In the answer try to provide as much text as possible from "response" section in the source document context without making much changes.
    If the answer is not found in the context, kindly state "I don't know." Don't try to make up an answer.

    CONTEXT: {context}

    QUESTION: {question}"""

    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=['context', 'question']
    )

    chain = RetrievalQA.from_chain_type(llm=llm,
                                        chain_type='stuff',
                                        retriever=retriever,
                                        input_key='query',
                                        return_source_documents=True,
                                        chain_type_kwargs={'prompt': PROMPT})
                    
    return chain

if __name__ == '__main__':
    create_vector_db()
    chain = get_qa_chain()
    print(chain.invoke('Do you have javasxript course?'))


