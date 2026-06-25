from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-small',
                         dimensions=32
                         )

response = embedding.embed_query("Virat Kohli is my faverite cricker")

print(str(response))
