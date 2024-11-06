from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from sentence_transformers import SentenceTransformer
from chromadb import PersistentClient
import fitz
from docx import Document
from typing import List
import os
import uvicorn
from tempfile import NamedTemporaryFile
from asyncio import to_thread
import logging

app = FastAPI()

CHROMA_DB_PATH = "./chromadb_storage"
chromadb_client = PersistentClient(path=CHROMA_DB_PATH)

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def extract_text_from_pdf(file_content: bytes) -> str:
    doc = fitz.open(stream=file_content, filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def extract_text_from_docx(file_content: bytes) -> str:
    with NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(file_content)
        temp_filename = temp_file.name

    doc = Document(temp_filename)
    text = "\n".join([para.text for para in doc.paragraphs])

    os.remove(temp_filename)

    return text

async def extract_text(file_content: bytes, filename: str) -> str:
    if filename.endswith(".pdf"):
        return await to_thread(extract_text_from_pdf, file_content)
    elif filename.endswith(".docx"):
        return await to_thread(extract_text_from_docx, file_content)
    elif filename.endswith(".txt"):
        return file_content.decode("utf-8")
    else:
        raise ValueError("Unsupported file format")

async def generate_embedding(text: str) -> list:
    return await to_thread(model.encode, text)

logging.basicConfig(level=logging.INFO)

@app.post("/ingest")
async def ingest_document(file: UploadFile = File(...)):
    try:
        content = await file.read()
        text = await extract_text(content, file.filename)
        embedding = await generate_embedding(text)

        # Log success
        logging.info(f"Document {file.filename} ingested successfully.")
        chromadb_client.store_document(content=text, embedding=embedding)
        return JSONResponse(content={"message": "Document ingested successfully"}, status_code=201)

    except ValueError as ve:
        logging.error(f"ValueError: {str(ve)}")
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        logging.error(f"Error during ingestion: {str(e)}")
        raise HTTPException(status_code=500, detail="An error occurred during ingestion")


@app.get("/query")
async def query_documents(user_query: str):
    try:
        query_embedding = model.encode(user_query)

        results = chromadb_client.query(query_embedding)

        return JSONResponse(content={"results": results}, status_code=200)

    except Exception as e:
        raise HTTPException(status_code=500, detail="An error occurred during querying")

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)