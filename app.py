import os
import vertexai
from vertexai.generative_models import GenerativeModel
import streamlit as st
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env file

st.title("Find your neighboring states")

users_state = st.text_input("Enter your state")

if users_state: 
    vertexai.init(project=os.environ.get("PROJECT_ID"), location="us-central1") 
    model = GenerativeModel("gemini-1.5-flash-002")
    response = model.generate_content(
        users_state
    )
    st.write(response.text) 
else:
    st.write("Please enter a state.") #display a message if no state is provided.
#st.header ("Hello Tech Exchange")
