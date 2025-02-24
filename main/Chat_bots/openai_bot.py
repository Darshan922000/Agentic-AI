from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser #its role is to parse(analyse) output generated by a language model and ensure it is in the expected string format
from langchain_openai import OpenAI
import streamlit as st 
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGSMITH_API_KEY")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

#Prompt-Template...
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are chemistry expert and you have to solve calculation based questions. Answer with proper calculation. Your name is D9AI. Created by Darshan. Please response to the user query in short"),
    ("user", "Question:{question}")
])

#Streamlit framework.....

st.title("D9AI")
input_text = st.text_input("Hi! How Can I Help You..")

# Open_AI...
llm = OpenAI(
    model="gpt-3.5-turbo-instruct",
    temperature=0,
    max_retries=2
)

#output_parser = StrOutputParser()
chain = prompt|llm #|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))
