from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_experimental.agents.agent_toolkits import create_csv_agent
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np
import seaborn as sns
import time


load_dotenv()

llm = ChatGoogleGenerativeAI(model = "gemini-2.0-flash")

agent=create_csv_agent(llm,"Bank-Records.csv",verbose=True,allow_dangerous_code=True)



ques = ""
res = agent.invoke(ques)
time.sleep(5)
print(res)