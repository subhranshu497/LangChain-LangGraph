from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

model = ChatAnthropic(
    model_name="claude-haiku-4-5-20251001",
    temperature=0.7,
    max_tokens=100
)

respone = model.invoke("Who is the prime minister of UK")

print(respone.content)