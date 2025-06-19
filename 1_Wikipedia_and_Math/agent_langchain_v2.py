# This is version 2 (modernized avoiding depricated metods) of the Agent.
# It can:
# - search Wikipedia
# - execute simple math.
# Example: the agent computes what (3 * AverageDogAge) equals to.
# ===========================================================================================
 
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv  # for getting the API_KEY from .env file
import os    # for getting the API_KEY from the environment
from langchain.chains.llm_math.base import LLMMathChain
from langchain.tools import Tool
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain.agents import initialize_agent, AgentType


# load API_KEY from .env file; initialize LLM
load_dotenv()  # load my Google Gemini key from .env file into environment
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")  # get Gemini key from environment
llm = GoogleGenerativeAI(
    google_api_key=GOOGLE_API_KEY,
    model="gemini-2.0-flash",
    temperature=0.2,
    max_tokens=500)

# Create math_chain
llm_math_chain = LLMMathChain.from_llm(llm)

# Wrap math_chain into a proper Tool
math_tool = Tool.from_function(
    name="Calculator",
    description="Useful for answering math questions.",
    func=lambda q: llm_math_chain.run(q)
)

# Use Wikipedia via load_tools
wiki_tools = load_tools(["wikipedia"], llm=llm)

# create a list of tools to be available to the agent
tools = [*wiki_tools, math_tool]

# Initialize agent
agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    handle_parsing_errors=True,
    verbose=True)


if __name__ == "__main__":
    # Use agent to access Wikipedia and do math
    user_query = "What is the average dog age? Multiply it by 3."
    result = agent.invoke(user_query)
    print(result)
