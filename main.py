#Libraries to be taken
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage
from langchain.prompts import ChatPromptTemplate
from langchain.prompts import HumanMessagePromptTemplate
import os

# Get Google Gemini setup

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
llm = ChatGoogleGenerativeAI(model="gemini-pro", convert_system_message_to_human=True)
chat_template = ChatPromptTemplate.from_messages([SystemMessage(content=("Think yourself as a Nutritionlist who is a Top Health fitness body trainer and gave answer according to content.")),HumanMessagePromptTemplate.from_template("{text}"),])

# Streamlit APP

st.set_page_config(page_title="Gemini model")
st.header(" My Dear Dr.Gemini Bodybuilder ")


# Input and submit button
input = st.text_input("Input:", key="input")
submit = st.button("▶")

# Display response when submit button is clicked
if submit and input:
    chat_message =  chat_template.format_messages(text=input)
    result = llm.invoke(chat_message)
    response = result.content
    
    st.subheader("The Response is")
    st.write(response)
