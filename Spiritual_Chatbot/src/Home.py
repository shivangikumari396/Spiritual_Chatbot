import os
import streamlit as st
import google.generativeai as genai
from streamlit_chat import message  # Ensure this import is present
from modules.embedder import Embedder
from modules.history import ChatHistory
from modules.layout import Layout
from modules.sidebar import Sidebar

# Initialize Layout and Sidebar
layout = Layout()
sidebar = Sidebar()

# Display header
layout.show_header("CSV")

# API key input
user_api_key = st.sidebar.text_input(
    label="#### Your Gemini API key 👇",
    placeholder="Paste your Gemini API key",
    type="password"
)

file_path = "C://Users//Abhinav Mishra//OneDrive//Desktop//Projects//Minor_Project//Bhagwad_Gita.csv"

# Initialize the Embedder class
embedder = Embedder()

# Check if the API key is provided and the file exists
if user_api_key and os.path.exists(file_path):
    genai.configure(api_key=user_api_key)  # Set the Gemini API Key
    vectors = embedder.getDocEmbeds(file_path=file_path, original_filename=os.path.basename(file_path))

    # Initialize chat history
    chat_history = ChatHistory()
    chat_history.initialize(os.path.basename(file_path))

    # Function to handle conversational chat using Gemini API
    def conversational_chat(query):
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(query)
        result = response.text  # Extracting the response
        st.session_state['history'].append((query, result))
        return result

    # Initialize session state for conversation history
    if 'history' not in st.session_state:
        st.session_state['history'] = []

    if 'generated' not in st.session_state:
        st.session_state['generated'] = [chat_history.default_prompt(os.path.basename(file_path))]

    if 'past' not in st.session_state:
        st.session_state['past'] = [chat_history.default_greeting()]

    # Containers for chat
    response_container = st.container()
    container = st.container()

    # User input form
    with container:
        with st.form(key='my_form', clear_on_submit=True):
            user_input = st.text_input("Query:", placeholder="Talk about your CSV data here (:", key='input')
            submit_button = st.form_submit_button(label='Send')

        if submit_button and user_input:
            output = conversational_chat(user_input)
            st.session_state['past'].append(user_input)
            st.session_state['generated'].append(output)

    # Display conversation history
    if st.session_state['generated']:
        with response_container:
            for i in range(len(st.session_state['generated'])):
                message(st.session_state["past"][i], is_user=True, key=str(i) + '_user', avatar_style="big-smile")
                message(st.session_state['generated'][i], key=str(i), avatar_style="thumbs")
else:
    layout.show_api_key_missing()  # Use layout to show message if API key is missing or file doesn't exist
