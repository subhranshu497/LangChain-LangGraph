from langchain_ollama import OllamaEmbeddings
from dotenv import load_dotenv

embeddings = OllamaEmbeddings(model='nomic-embed-text',
                              dimensions=256
                              )
documents = [
    "I live in chicago",
    "My family stays in Phoenix",
    "I love to stay in SFO",
    "My mom stays in Khunta"
]

vector = embeddings.embed_documents(documents)

print(str(vector))