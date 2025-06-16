# This is version 3: modernized, LangChain_LangGraph refactored,
# and avoids depricated metods. The Agent that can:
# - search Wikipedia
# - execute simple math.
# Example: the agent computes what (3 * AverageDogAge) equals to.
# I also Triggering CI test for v3
# ===========================================================================================

from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from langchain_community.tools.wikipedia.tool import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langgraph.prebuilt import create_react_agent
from langgraph.prebuilt.chat_agent_executor import AgentState
from langgraph.graph import StateGraph
from langchain_core.messages import get_buffer_string
from nltk.tokenize import sent_tokenize, word_tokenize
# import nltk
# nltk.download(['punkt', 'punkt_tab'])

load_dotenv()  # Try to load local .env file (for local dev); silently skip if not found (for CI)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")  # Get API key from environment
if GEMINI_API_KEY is None:
    raise ValueError("❌ GEMINI_API_KEY not found. Make sure it's in your .env file or set as a GitHub Action secret.")
else:
    print("✅ GEMINI_API_KEY loaded successfully (not printing it for security).")

# 1. SETUP LLM
llm = ChatGoogleGenerativeAI(
    google_api_key=GEMINI_API_KEY,
    model="gemini-2.0-flash",
    temperature=0.3,
    max_tokens=1024,
)


# 2. DEFINE TOOLS
@tool
def calculator(expression: str) -> str:
    """Use this for math expressions, like multiplication or addition."""
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Error: {str(e)}"


# Wikipedia tool (wrapping properly)
wiki_tool = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())

# Creting a list od tools for the agent
tools = [calculator, wiki_tool]

# 3. CREATE LangGraph ReAct AGENT
agent_node = create_react_agent(llm, tools, state_schema=AgentState)

# 4. BUILD WORKFLOW GRAPH
workflow = StateGraph(state_schema=AgentState)
workflow.add_node("agent", agent_node)
workflow.set_entry_point("agent")
workflow.set_finish_point("agent")

# 5. COMPILE
graph = workflow.compile()

if __name__ == "__main__":
    # 6. RUN
    user_query = "What is the average dog age? Multiply it by 3."
    response = graph.invoke(
        {"messages": [("user", user_query)]}
        )

    # 7. INTERPRET RESPONSE
    # Safely extract all message content
    final_agent_message = get_buffer_string(response["messages"])
    print("\nFinal Agent Message:\n", final_agent_message)

    # 7. EXTRACT THE ANSWER
    print("\n___Final Agent Message:\n", sent_tokenize(final_agent_message)[-1])
    print("\n___Answer:", word_tokenize(final_agent_message)[-2])
