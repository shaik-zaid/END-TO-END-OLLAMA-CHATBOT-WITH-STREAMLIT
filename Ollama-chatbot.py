import os
from dotenv import load_dotenv
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

load_dotenv()


#Langsmith Tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")


#Prompt Template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please respond to the user question."),
        ("user", "Question:{question}"),
    ]
)

def generate_response(question,llm):
    llm=Ollama(model=llm)
    output_parser=StrOutputParser()
    chain=prompt | llm | output_parser
    answer=chain.invoke({"question":question})
    return answer


## Streamlit 
## Title of the app
st.title("Q&A Chatbot with Ollama")

#Title for model selection 
st.sidebar.title("Model Settings")

## Drop down to select various Open AI models
llm=st.sidebar.selectbox("Select Ollama model",["gemma:2b","llama3","mistral"])


## Main interface for user input
st.write("Go ahead and ask any question!")
user_input=st.text_input("You:")

if user_input:
    response=generate_response(user_input,llm)
    st.write(response)
else:
    st.write("Please enter a question to get a response.")
    
    
    

