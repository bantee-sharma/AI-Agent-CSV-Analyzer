from langchain_experimental.agents.agent_toolkits import create_csv_agent
from langchain.agents import AgentType
from langchain_experimental.utilities import PythonREPL
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

load_dotenv()


st.title("CSV analysis")
uploaded_file = st.file_uploader("Choose a file",type=["csv"])

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)
    st.write("Data Frame")
    st.dataframe(df)

    with open("temp","wb") as f:
        f.write(uploaded_file.getbuffer())

    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")



    agent = create_csv_agent(
        llm=llm,
        path="temp",
        verbose=True,
        allow_dangerous_code=True,
        handle_parsing_errors=True)
    

    user_input = st.text_input("Ask anything about this file")
    if st.button("Submit"):
        
        response = agent.run(user_input)
        st.write(response)