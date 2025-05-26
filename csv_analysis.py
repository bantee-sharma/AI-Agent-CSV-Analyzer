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



st.header("Csv Analysis")
uploaded_file = st.file_uploader("Choose a file",type=["csv"])

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)
    st.write("Data Preview")
    st.dataframe(df)

    with open("temp_uploaded.csv", "wb") as f:
            f.write(uploaded_file.getbuffer())

    llm = ChatGoogleGenerativeAI(model = "gemini-2.0-flash")

    agent  = create_csv_agent(
        llm=llm,
        path="temp_uploaded.csv",
        verbose=True,allow_dangerous_code = True
    )



    user_query = st.text_input("Ask something about the CSV data:")
    if st.button("Submit"):
        response = agent.run(user_query)
        st.write(response)
