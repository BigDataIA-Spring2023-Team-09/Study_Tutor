import os
import streamlit as st
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

# Set page title
st.markdown("<h1 style='text-align: center;'>STUDY TUTOR</h1>", unsafe_allow_html=True)
st.header("")

# Create a text input for user to enter their name
input_text = st.text_input("Enter Text")

summarize = 'Summarize this for a second-grade student:\n\n'

grammar = 'Correct this to standard English:\n\n'

keywords = 'Extract keywords from this text:\n\n'

interview = 'Create a list of 8 questions for an interview from:\n\n'

result = ''


def completion_openai_call(api_prompt, user_prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt = api_prompt + user_prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response


# Create four buttons in a column with different layout functions
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("Summarize"):
        if input_text == "":
            result = 'Please enter some text.'
        else:
            temp = completion_openai_call(summarize, input_text)
            result = temp['choices'][0]['text']

with col2:
    if st.button("Grammar Corrections"):
        if input_text == "":
            result = 'Please enter some text.'
        else:
            temp = completion_openai_call(grammar, input_text)
            result = temp['choices'][0]['text']
with col3:
    if st.button("Extract keywords"):
        if input_text == "":
            result = 'Please enter some text.'
        else:
            temp = completion_openai_call(keywords, input_text)
            result = temp['choices'][0]['text']
with col4:
    if st.button("Generate Interview Questions"):
        if input_text == "":
            result = 'Please enter some text.'
        else:
            temp = completion_openai_call(interview, input_text)
            result = temp['choices'][0]['text']

st.header("")
if result is not None:
    st.write(result)

