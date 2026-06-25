from langchain_voyageai import VoyageAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = VoyageAIEmbeddings(model='voyage-4-lite',
                                output_dimension=256
                                )

documents = [
    "I live in chicago",
    "My family stays in Phoenix",
    "I love to stay in SFO",
]
result = embeddings.embed_documents(documents)

print(str(result))
