import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

key = os.getenv('GROQ_API_KEY')
parser = StrOutputParser()

Model = 'llama-3.1-8b-instant'
model = ChatGroq(api_key=key,model=Model )

llm = model | parser
print(llm.invoke("what is chlroophyll?"))