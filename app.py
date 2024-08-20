import os 
from dotenv import load_dotenv 
import streamlit as st 
import google.generativeai as genai 
#load enviroment variable 
load_dotenv()
google_api=os.getenv("GOAGLE_API_KEY")

if google_api:
    genai.configure(api_key=google_api)
else:
    st.error("google api not coorect")

def generate_text(input):
    model=genai.GenerativeModel("gemini-pro")
    response=model.generate_content(input)
    return response.text 

st.title("check if body is sutibale or not  ")
user_input=st.text_area("enter ur weighte ")

user_input=st.text_area("enter ur  heighte")

if st.button("generate response "):
    if user_input:
        response_text=generate_text(user_input)
        if response_text:
            st.subheader("ai response")
            st.write(response_text)
    else:
        st.error("please enter some text")        
