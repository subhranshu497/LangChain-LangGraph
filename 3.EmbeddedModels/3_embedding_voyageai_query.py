from langchain_voyageai import VoyageAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = VoyageAIEmbeddings(model='voyage-4-lite',
                                output_dimension=256
                                )

query = "I love to eat Maggie"
result = embeddings.embed_query(query)

print(str(result))
