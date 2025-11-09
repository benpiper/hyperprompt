import os
import json
import logging
import time
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("hyperprompt")

llm = ChatOpenAI(model="gpt-5-nano", temperature=1,
                 use_responses_api=True, reasoning_effort="low")

SYSTEM_PROMPT = """
    You are a hyperprompt agent.
    Take the user's prompt and use it to construct an improved, enriched prompt that better articulates the user's intention. This is called the hyperprompt.
    Infer the user's intention and express it in the hyperprompt.
    Do not repeat the user's prompt verbatim.
    Do not answer the user's prompt directly.
    Do not include any information that would answer the user's prompt.
    Do not make any reference to the fact that you are generating a prompt.
    Do not generate a system prompt. Only generate a user prompt.
    Do not ask clarifying questions.
    Do not be prescriptive.
    Do not make assumptions or recommendations.
    The length of the hyperprompt must roughly match the length of the user's prompt.
    If the user's prompt is short, make the hyperprompt short.
    If the user's prompt is long, make the hyperprompt long.
    Respond only with the hyperprompt.
"""

USER_PROMPT = """
make green tea from pellets
"""

prompt_template = ChatPromptTemplate.from_messages([
    ("system", SYSTEM_PROMPT),
    ("user", "{user_prompt}")
])

# Invoke the hyperprompt_chain if you just want the hyperprompt
hyperprompt_chain = prompt_template | llm | StrOutputParser()
result = hyperprompt_chain.invoke({"user_prompt": USER_PROMPT})

# Invoke the full chain if you want the hyperprompt fed back into the LLM
full_chain = prompt_template | llm | StrOutputParser() | llm
# result = full_chain.invoke({"user_prompt": USER_PROMPT})

logging.info(result)
