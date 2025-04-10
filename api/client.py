import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")


def get_ollama_poem(input_poem):
    response = requests.post(
        "http://localhost:8000/poem/invoke",
        json={'input':{'topic':input_poem}})
    
    return response.json()['output']


def get_ollama_essay(input_essay):
    response = requests.post(
        "http://localhost:8000/essay/invoke",
        json={'input':{'topic':input_essay}})
    
    return response.json()['output']


st.title("Langchain Demo With Ollama API")
input_poem=st.text_input("Write a poem about the topic")
input_essay=st.text_input("Write an essay about the topic")

if input_poem:
    st.write(get_ollama_poem(input_poem))
    
if input_essay:
    st.write(get_ollama_essay(input_essay))