import os

from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.prompts import HumanMessagePromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Instantiate the LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-pro",
    google_api_key=GOOGLE_API_KEY,
    verbose=True,
    temperature=0.7,
    convert_system_message_to_human=True
)

# Define a prompt template
prompt = ChatPromptTemplate.from_messages(
     [
        SystemMessage(
            content=(
                "Generate a list of 10 synonyms for the following word. Return the results as a comma seperated list."
            )
        ),
        HumanMessagePromptTemplate.from_template("{input}"),
    ]
)

# Create LLM chain
chain = prompt | llm

response = chain.invoke({"input": "happy"})
print(response)