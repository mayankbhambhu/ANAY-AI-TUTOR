import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma

# Load the API key from the .env file
load_dotenv()

print("Loading PDF...")
loader = PyPDFLoader("document.pdf")
data = loader.load()

print("Splitting text...")
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = text_splitter.split_documents(data)

print("Creating database...")
embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
# This creates a folder called 'chroma_db' in your project
vectorstore = Chroma.from_documents(
    documents=chunks, 
    embedding=embeddings,
    persist_directory="./chroma_db"
)

print("✅ Database created successfully! You can now run the app.")