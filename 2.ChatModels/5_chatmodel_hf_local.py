from langchain_ollama import ChatOllama

model = ChatOllama(model='llama3.2:3b',
                 temperture=0.6,
                 num_predict=100
                 )

response = model.invoke("What is the capital of Uganda")
print(response.content)