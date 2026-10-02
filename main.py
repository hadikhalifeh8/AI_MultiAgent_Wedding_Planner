from prompts import WEDDING_PLANNER_AGENT_PROMPT, USER_PROMPT_FOR_MAIN_AGENT
from langchain.agents import create_agent
from models import openai_model
from agents import delegate_to_sub_agent1, delegate_to_sub_agent2
import logging
from langchain.messages import HumanMessage


# configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s |  %(levelname)s | %(message)s"
)

# asking user for requirements for their wedding planning
logging.info("Asking user for their wedding planning requirements...")
user_requirements = input("Please enter your wedding planning requirements: \n")

# updating the system prompt
updated_system_prompt = WEDDING_PLANNER_AGENT_PROMPT.format(requirements=user_requirements)

# Creating the main agent
logging.info("Initializing Main Agent...")
main_agent = create_agent(
    model=openai_model,
    tools=[delegate_to_sub_agent1, delegate_to_sub_agent2],
    name="MainAgent",
    system_prompt=updated_system_prompt
)

#ested3a2  l main agent
# invoke the main agent with the user prompt
logging.info("Invoking Main Agent ...")
response_main_agent =  main_agent.invoke({"messages": [HumanMessage(content=USER_PROMPT_FOR_MAIN_AGENT)]})

# printing the response from the main agent
print("\nMain Wedding Planner Agent Response: ")
print(response_main_agent["messages"][-1].content)