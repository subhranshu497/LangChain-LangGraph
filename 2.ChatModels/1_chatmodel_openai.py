from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

model = ChatOpenAI_model = ChatOpenAI(
    model_name="gpt-4o",  # Specify the model name
    temperature=0.7,      # Set the temperature for response variability
)

response = model.invoke("Hello, how are you today?")  # Invoke the model with a prompt
print(response.content)  # Print the response content
