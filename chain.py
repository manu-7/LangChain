from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

load_dotenv()

prompt = PromptTemplate(
    template='Generate 5 interesting facts about {topic}',
    input_variables=['topic']
)

llm=Ollama(model="phi")

parser = StrOutputParser()

chain = prompt | llm | parser

result = chain.invoke({'topic':'cricket'})

print(result)

chain.get_graph().print_ascii()