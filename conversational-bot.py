import os

from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.prompts import HumanMessagePromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage

from langchain.prompts import PromptTemplate
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Instantiate the LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-pro",
    google_api_key=GOOGLE_API_KEY,
    verbose=True
)



PROMPT_TEMPLATE = """The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know.

Current conversation:
{history}
Human: {input}
AI Assistant:
"""

PROMPT = PromptTemplate(
    input_variables=["history", "input"], template=PROMPT_TEMPLATE
)

conversation = ConversationChain(
    llm=llm,
    # verbose=True,
    prompt=PROMPT,
    memory=ConversationBufferMemory(ai_prefix="AI Assistant")
)

# conversation.predict(input="who is Gojo?")
# conversation.predict(input="")

while True:
    human = input()
    response = conversation.predict(input=human)
    print(response)