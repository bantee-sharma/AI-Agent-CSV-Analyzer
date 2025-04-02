from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import Agent,agent_types,initialize_agent,AgentType
from langchain.tools import Tool
from dotenv import load_dotenv
from langchain_experimental.agents.agent_toolkits import create_csv_agent
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

load_dotenv()


llm = ChatGoogleGenerativeAI(model = "gemini-2.0-flash")

agent  = create_csv_agent(
    llm, "Bank-Records.csv",
    verbose=True,allow_dangerous_code = True
)

res = agent.invoke({"input": "Draw a bar plot of count of peole in each country"})

print(res)