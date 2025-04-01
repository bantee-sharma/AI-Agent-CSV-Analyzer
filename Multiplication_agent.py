from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import initialize_agent,AgentType
from langchain.tools import Tool
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(model = "gemini-2.0-flash")

input = input()
def func(input):
    a,b = map(int, input.replace(","," ").split())
    return a + b

multiply_tool = Tool(
    name="MultiplyNumbers",
    func = func,
    description="Add two numbers a and b"
)

tools = [multiply_tool]
agent = initialize_agent(
    llm = llm,
    tools = tools,
    agent_type = AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
    verbose = True
)


query = "what is result of addition of a and b"
res = agent.invoke(query)
print(res)