from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from llama_index.llms.groq import Groq
from llama_index.core import VectorStoreIndex,SimpleDirectoryReader,ServiceContext,PromptTemplate
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from pydantic import BaseModel
from crawl import crawl_url
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

# Load variables from .env file
load_dotenv()

api_key = os.getenv("API_KEY")
host = os.getenv("HOST")


#setup llm
llm = Groq(model="mixtral-8x7b-32768", api_key=api_key)

#load embedding models
embed_model = HuggingFaceEmbeddings()
print(embed_model)
#setup service context
service_context = ServiceContext.from_defaults(
    chunk_size=4000,
    llm=llm,
    embed_model=embed_model
)
print(service_context)

app = FastAPI()

# CORS middleware to allow all origins

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*","http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Url(BaseModel):
    url: str

@app.post("/crawl/")
async def create_item(url: Url):
    crawl_url(url.url)
    return "data crawled"

@app.websocket("/chat")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    # load document
    documents = SimpleDirectoryReader("F:/talkwithdoc/data/").load_data()
    print("document :- ", documents)

    # indexing models
    index = VectorStoreIndex.from_documents(documents, service_context=service_context)
    print("index :- ", index)

    # setup query engine
    query_engine = index.as_query_engine()
    try:
        while True:
            data = await websocket.receive_text()
            response = query_engine.query(data)
            await websocket.send_text(f"Response was: {response}")
    except WebSocketDisconnect as e:
        print(f"Client disconnected {e}")

# Run the app with Uvicorn server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=host, port=64)
