from langchain_ollama import OllamaEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embeddings = OllamaEmbeddings(model='nomic-embed-text',
                              dimensions=256
                              )
documents = [
    "I live in chicago",
    "My family stays in Phoenix",
    "I love to stay in SFO",
    "My mom stays in Khunta"
]

query="Tell me about my family"

doc_embedding = embeddings.embed_documents(documents)
query_embedding = embeddings.embed_query(query)

score = cosine_similarity([query_embedding], doc_embedding)[0]
index, score =sorted(list(enumerate(score)),key=lambda x:x[1])[-1]

print(query)
print(documents[index])
print("similarity score is: ", score)

