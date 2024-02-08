import os

from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate


GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Instantiate the LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-pro",
    google_api_key=GOOGLE_API_KEY,
    verbose=True,
    temperature=0.7,
)

# Define a prompt template
prompt = ChatPromptTemplate.from_template("Tell me a joke about {subject}")

# Create LLM chain
chain = prompt | llm

response = chain.invoke({"subject": "cat"})
print(response)