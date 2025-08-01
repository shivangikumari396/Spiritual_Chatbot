import os
import pandas as pd
import streamlit as st
import google.generativeai as genai

from modules.chatbot import Chatbot
from modules.embedder import Embedder

class Utilities:

    @staticmethod
    def load_api_key():
        """
        Loads the Gemini API key from the .env file or 
        from the user's input and returns it.
        """
        if not hasattr(st.session_state, "api_key"):
            st.session_state.api_key = None
        
        # You can define your API key in .env directly
        if os.path.exists(".env") and os.environ.get("GEMINI_API_KEY") is not None:
            user_api_key = os.environ["GEMINI_API_KEY"]
            st.sidebar.success("API key loaded from .env", icon="🚀")
        else:
            if st.session_state.api_key is not None:
                user_api_key = st.session_state.api_key
                st.sidebar.success("API key loaded from previous input", icon="🚀")
            else:
                user_api_key = st.sidebar.text_input(
                    label="#### Your Gemini API key 👇", placeholder="Enter your Gemini API key", type="password"
                )
                if user_api_key:
                    st.session_state.api_key = user_api_key

        return user_api_key

    @staticmethod
    def setup_chatbot(uploaded_file, model, temperature):
        """
        Setup the chatbot using the provided file and model details, using Gemini API.
        """
        embeds = Embedder()

        with st.spinner("Processing..."):
            if uploaded_file.name.endswith(".csv"):
                # Read and process CSV file content
                df = pd.read_csv(uploaded_file)
                # Convert CSV content into a text format suitable for embeddings
                file_content = df.to_string(index=False)
            else:
                st.error("Unsupported file type. Only CSV is allowed for this setup.")
                return None
            
            # Get the document embeddings for the CSV content
            vectors = embeds.getDocEmbeds(file_content, uploaded_file.name)

            # Create a Chatbot instance with the specified model and temperature
            chatbot = Chatbot(model, temperature, vectors, api_key=st.session_state.api_key)
        
        st.session_state["ready"] = True

        return chatbot
