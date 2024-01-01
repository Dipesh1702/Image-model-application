from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#function to load model and get response

model = genai.GenerativeModel("gemini-pro")
chat=model.start_chat(history=[])

def get_gemini_response(question):
    response=chat.send_message(question,stream=True)
    return response

#initialize streamlit app
st.set_page_config(page_title="chatbot demo")
st.header("Gemini llm application")

#inatilize session state for chat histroy if it dont exist

if 'chat_history' not in st.session_state:
    st.session_state['chat_history']=[]

input = st.text_input("input: ",key="input")
submit=st.button("ask the question")

if submit and input:
    response=get_gemini_response(input)
    #add user query and response to session chat
    st.session_state['chat_history'].append(("you",input))
    st.subheader("The response is")
    
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot",chunk.text))

st.subheader("The chat History is ")

for role,text in st.session_state['chat_history']:
    st.write(f"{role}:{text}")


