# Agent that can search Wikipedia and execute simple math.
# Example: the agent computes what (3 * AverageDogAge) equals to.
# ===========================================================================================

from langchain_google_genai import GoogleGenerativeAI
# alternatively use OpenAI: from langchain.llms import OpenAI

from dotenv import load_dotenv  # for getting the API_KEY from .env file
import os  # for getting the API_KEY from the environment

# pip install -U langchain-community
from langchain_community.agent_toolkits.load_tools import load_tools
# OLD: from langchain.agents import load_tools

from langchain.agents import initialize_agent
from langchain.agents import AgentType


# load API_KEY
load_dotenv()  # load my Google Gemini key from .env file into environment
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")  # get Gemini key from environment


def langchain_agent(user_query="What is the average dog age? Multiply it by 3."):
    llm = GoogleGenerativeAI(
        google_api_key=GEMINI_API_KEY, model="gemini-2.0-flash",
        temperature=0.5,
        max_tokens=1_000)
    tools = load_tools(["wikipedia", "llm-math"], llm=llm)
    agent = initialize_agent(
        tools,
        llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True)
# Alternative:
#   agent = initialize_agent(
#   tools,
#   llm,
#   agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
#   verbose=True,
#   handle_parsing_errors=True)

    result = agent.invoke(user_query)
    return result


if __name__ == "__main__":
    user_query = "What is the average dog age? Multiply it by 3."
    print(langchain_agent(user_query))
