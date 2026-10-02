from langchain.agents import create_agent
from langchain.tools import tool
from langchain.messages import HumanMessage
from models import openai_model
from tools import search_web
import logging

# configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s |  %(levelname)s | %(message)s"
)

#Creating SubAgents
logging.info("initialize SubAgent1...")
sub_agent1 = create_agent(model=openai_model, tools=[search_web], name="SubAgent1")

logging.info("initialize SubAgent2...")
sub_agent2 = create_agent(model=openai_model, tools=[search_web], name="SubAgent2")

@tool
def delegate_to_sub_agent1(query: str) -> str:
    """ Search the web for a given topic by delegating the task to SubAgent1 to do so"""
    logging.info(f"Delegating query to SubAgent1: {query}")
    response = sub_agent1.invoke({"messages": [HumanMessage(content=query)]})
    return response["messages"][-1].content

@tool
def delegate_to_sub_agent2(query: str) -> str:
    """ Search the web for a given topic by delegating the task to SubAgent2 to do so"""
    logging.info(f"Delegating query to SubAgent2: {query}")
    response = sub_agent2.invoke({"messages": [HumanMessage(content=query)]})
    return response["messages"][-1].content