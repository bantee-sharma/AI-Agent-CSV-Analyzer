from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import Agent,agent_types,initialize_agent,AgentType
from langchain.tools import Tool
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(model = "gemini-2.0-flash")

def get_weather(location):
    return f"The weather in {location} is 25*C"

weather_tool = Tool(
    name = "Get_Weather",
    func = get_weather,
    description="Provides the weather information for a given location. Input should be location. Return the weather Information"
)

tools = [weather_tool]
agent = initialize_agent(
    llm = llm,
    tools = tools,
    agent_type = AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
    verbose = True
)

query = "Who is the pm of india."
res = agent.invoke(query)
print(res)