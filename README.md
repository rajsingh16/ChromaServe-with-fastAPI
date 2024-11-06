# ChromaServe-with-fastAPI
An intelligent document management and retrieval-augmented generation (RAG) solution, this project combines ChromaDB’s efficient embedding storage with FastAPI’s high-performance capabilities. It supports document types such as PDF, DOCX, and TXT. The server allows users to ingest documents, extract their contents, generate embeddings, and query the stored documents efficiently.

# Requirements
Python 3.9 or higher
FastAPI
ChromaDB
Sentence-Transformers
Uvicorn (for running the server)

# Setup
1.Clone the repository:
'''bash
git clone https://github.com/rajsingh16/ChromaServe-with-fastAPI
'''
2. Install the dependences:
   '''bash
   pip install -r requirements.txt
    '''
3. Run the server:
Start the FastAPI server with the following command:
'''bash
uvicorn main:app --reload
'''
The server will run on http://127.0.0.1:8000.
# Endpoints
POST /ingest
Ingest a document (PDF, DOCX, or TXT) and store its text and embedding in ChromaDB.

Request
Content-Type: multipart/form-data
File: The document file to ingest (PDF, DOCX, or TXT).

Example Request:
'''bash
curl -X 'POST' \
  'http://127.0.0.1:8000/ingest' \
  -F 'file=@your-document.pdf'

'''

Here’s a sample README.md for your FastAPI project that implements Retrieval-Augmented Generation (RAG) using ChromaDB and Hugging Face's SentenceTransformer:

FastAPI RAG Server with ChromaDB and Sentence-Transformers
This project implements a lightweight FastAPI server for Retrieval-Augmented Generation (RAG) using ChromaDB's Persistent Client for ingesting and querying documents, and Sentence-Transformers from Hugging Face for embedding generation. It supports document types such as PDF, DOCX, and TXT. The server allows users to ingest documents, extract their contents, generate embeddings, and query the stored documents efficiently.

Features
Document Ingestion: Upload and ingest documents in PDF, DOCX, and TXT formats. The text from the document is extracted and embedded using Sentence-Transformers.
Querying: Send a user query to search through ingested documents using embeddings.
ChromaDB: Persistent document storage with efficient querying and retrieval based on embeddings.
Asynchronous Processing: Non-blocking endpoints with support for concurrent requests using FastAPI and Python’s asyncio.
Requirements
Python 3.9 or higher
FastAPI
ChromaDB
Sentence-Transformers
Uvicorn (for running the server)
You can install the required dependencies using pip:

bash
Copy code
pip install fastapi chromadb sentence-transformers uvicorn
For processing PDF and DOCX files, the following libraries are used:

PyMuPDF (for PDF text extraction)
python-docx (for DOCX text extraction)
Install these dependencies as well:

bash
Copy code
pip install pymupdf python-docx
Setup
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/fastapi-rag-server.git
cd fastapi-rag-server
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the server:

Start the FastAPI server with the following command:

bash
Copy code
uvicorn main:app --reload
The server will run on http://127.0.0.1:8000.

Endpoints
POST /ingest
Ingest a document (PDF, DOCX, or TXT) and store its text and embedding in ChromaDB.

Request
Content-Type: multipart/form-data
File: The document file to ingest (PDF, DOCX, or TXT).
Example Request:
bash
Copy code
curl -X 'POST' \
  'http://127.0.0.1:8000/ingest' \
  -F 'file=@your-document.pdf'
Response
Status Code: 201 (Created)
Body: { "message": "Document ingested successfully" }
GET /query
Query ingested documents using a user query string. This endpoint uses the embeddings generated from the query to retrieve relevant documents.

Request
Query Parameters: user_query (string) — The query string.
Example Request:
'''bash
curl -X 'GET' \
  'http://127.0.0.1:8000/query?user_query=your+search+query'
'''
Response
Status Code: 200 (OK)
Body: A JSON object containing the query results.
Example:
'''json
{
  "results": [
    {
      "document_id": "1",
      "score": 0.89,
      "content": "Extracted content of the matching document..."
    }
  ]
}
'''
# Technologies Used
FastAPI: For building the lightweight and high-performance web API.
ChromaDB: For persistent document storage and efficient query handling based on embeddings.
Sentence-Transformers: For generating text embeddings to represent the content of documents and queries.
Uvicorn: ASGI server to run the FastAPI app.
PyMuPDF (fitz): For extracting text from PDF files.
python-docx: For extracting text from DOCX files.

# License
This project is licensed under the MIT License - see the LICENSE file for details.
