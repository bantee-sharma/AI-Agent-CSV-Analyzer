from langchain_experimental.agents.agent_toolkits import create_csv_agent
from langchain.agents import AgentType
from langchain_experimental.utilities import PythonREPL
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import pandas as pd
import numpy as np

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")


agent = create_csv_agent(
    llm=llm,
    path="Bank-Records.csv",
    verbose=True,
    allow_dangerous_code=True,
    
)

query = "total number of people who have credit sore greater than 500"
response = agent.invoke(query)
print(response)