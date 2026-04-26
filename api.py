from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

app = FastAPI()

# This allows your HTML file to talk to this Python server securely
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Setup AI Chain (Same logic as before)
embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
vectorstore = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.1)

template = """You are a direct tutor.
Context: {context}
Question: {question}
Answer:"""
QA_PROMPT = PromptTemplate.from_template(template)

tutor_chain = (
    {"context": retriever | (lambda docs: "\n\n".join(d.page_content for d in docs)), "question": RunnablePassthrough()}
    | QA_PROMPT | llm | StrOutputParser()
)

# Define the data format we expect from the website
class UserQuestion(BaseModel):
    question: str

# Define the exact URL endpoint our website will call
@app.post("/ask")
def ask_tutor(data: UserQuestion):
    print(f"Website asked: {data.question}")
    answer = tutor_chain.invoke(data.question)
    return {"reply": answer}