from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import Agent,agent_types,initialize_agent,AgentType
from langchain.tools import Tool
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(model = "gemini-2.0-flash")

while True:
    user_input = input("You: ")
    if user_input == ['exit',"quit"]:
        print("Good Bye")
        break 
    res = llm.invoke(user_input)
    print(res.content)