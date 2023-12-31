from dotenv import load_dotenv
load_dotenv()#loading all enviroment veriables

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#function to load gemini model
model=genai.GenerativeModel("gemini-pro-vision")
def get_gemini_response(input,image):
    if input!="":
        response=model.generate_content([input,image])
    else:
        response=model.generate_content(image)
    return response.text

#initializing stramlit
st.set_page_config(page_title="gemini image demo")
st.header("Gemini LLM applicatiom")
input=st.text_input("Input prompt: ",key="input")

#image upload option
upload_file=st.file_uploader("Choose Image...",type=["jpg","jpng","png"])
image=""
if upload_file is not None:
    image=Image.open(upload_file)
    st.image(image,caption="Uploaded image.",use_column_width=True)


submit=st.button("Tell me about image")

#if submit is clicked
if submit:
    response=get_gemini_response(input,image)
    st.subheader("The Response is")
    st.write(response)
