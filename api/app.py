from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
from langserve import add_routes
import os
import uvicorn
from dotenv import load_dotenv

load_dotenv()
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
app = FastAPI(
    title="Langchain API",
    description="Langchain API with Ollama LLM",
    version="1.0"
)

# Prompt Template

llm=Ollama(model="mistral:7b-instruct-v0.3-q2_K")

prompt1=ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words")
prompt2=ChatPromptTemplate.from_template("Write me an poem about {topic} for a 5 years child with 100 words")


# add_routes
add_routes(
    app,
    prompt2|llm,
    path="/poem"
)

add_routes(
    app,
    prompt1|llm,
    path="/essay"
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)