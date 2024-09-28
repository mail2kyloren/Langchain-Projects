from langchain_community.llms import OpenAI
from dotenv import load_dotenv

import os

load_dotenv() #This is to load the .env file into the environment'''

import streamlit as st

#The below statements should be called before the get_openai_response function.Thats
#why it was giving the blank page

st.set_page_config(page_title= "Q&A demo")
st.header("Langchain Application")

## Function to load OpenAI model andto get the response.

def get_openai_response(question):
    llm=OpenAI(openai_api_key=os.environ.get("OPEN_API_KEY"),model_name="gpt-3.5-turbo-instruct",temperature=0.5)
    response = llm(question)
    return response 

#initialize our streamlit app

input = st.text_input("Input: ", key="input")
response = get_openai_response(input)

submit=st.button("Ask the question..")

#if ask button is called

if submit:
    st.subheader("The Response is")
    st.write(response)
