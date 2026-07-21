import os
from pathlib import Path
from dotenv  import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages  import SystemMessage, HumanMessage
from langchain_community.document_loaders import TextLoader

#  loading  .env and model name
env_path=Path(__file__).parent /".env"
load_dotenv(dotenv_path=env_path)
model =  os.environ["model_name"]

#  creating llm instance
llm =  ChatGroq(
    model =  model,
    temperature=0
)

print("-"*30)
print("Simple Memory Chatbot")
print("-"*30)

while  True:
    loader = TextLoader("memory.txt", encoding='utf-8')
    docs = loader.load()

    memory = docs[0].page_content

    #  user input
    user  = input("user: ")
    if  user.lower() == 'exit':
        break

    prompt = [
        SystemMessage(
            content=(
                f"Previous conversation:\n{memory}\n\n"
                "You are a helpful AI assistant. "
                "Your job is to answer the user's questions clearly and helpfully. "
                "Use the previous conversation when it is relevant to the current request. "
                "If the context is empty or unrelated, respond naturally. "
                "Be concise, accurate, and friendly."
            )
        ),
        HumanMessage(content=user)
    ]

    #  Genrate response
    response = llm.invoke(prompt)
    print(f"\nAI: {response.content}")

    # adding chat history in a fle
    with open("memory.txt",  "a",encoding='utf-8') as f:
        f.write(f"\nUser: {user}\n")
        f.write(f"\nAI: {response.content}\n")