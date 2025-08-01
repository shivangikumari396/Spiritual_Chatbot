import streamlit as st
from streamlit_chat import message

class ChatHistory:
    
    def __init__(self):
        # Initialize history from session state or an empty list
        self.history = st.session_state.get("history", [])
        st.session_state["history"] = self.history

    def default_greeting(self):
        return "Hey Assistant ! 👋"

    def default_prompt(self, topic):
        return f"Hello ! Ask me anything about {topic} 🤗"

    def initialize_user_history(self):
        # Initialize user messages if not already present in session state
        if "user" not in st.session_state:
            st.session_state["user"] = [self.default_greeting()]

    def initialize_assistant_history(self, uploaded_file_name):
        # Initialize assistant messages if not already present in session state
        if "assistant" not in st.session_state:
            st.session_state["assistant"] = [self.default_prompt(uploaded_file_name)]

    def initialize(self, uploaded_file_name):
        # Initialize both user and assistant histories
        self.initialize_assistant_history(uploaded_file_name)
        self.initialize_user_history()

    def reset(self, uploaded_file_name):
        # Clear the chat history
        st.session_state["history"] = []
        st.session_state["reset_chat"] = False

        # Reinitialize user and assistant history after reset
        self.initialize_user_history()
        self.initialize_assistant_history(uploaded_file_name)

    def append(self, mode, message_text):
        # Append messages to session state, either "user" or "assistant"
        if mode in st.session_state:
            st.session_state[mode].append(message_text)

    def generate_messages(self, container):
        # Generate the chat messages in the UI
        if st.session_state.get("assistant"):
            with container:
                for i in range(len(st.session_state["assistant"])):
                    message(
                        st.session_state["user"][i],
                        is_user=True,
                        key=f"history_{i}_user",
                        avatar_style="big-smile",
                    )
                    message(st.session_state["assistant"][i], key=str(i), avatar_style="thumbs")


