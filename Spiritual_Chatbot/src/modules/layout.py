import streamlit as st

class Layout:
    
    def show_header(self, types_files="CSV"):
        """
        Displays the header of the app
        """
        st.markdown(
            f"""
            <h1 style='text-align: center;'> Ask about Bhagwad Gita</h1>
            """,
            unsafe_allow_html=True,
        )

    def show_api_key_missing(self):
        """
        Displays a message if the user has not entered an API key for Google Gemini API
        """
        st.markdown(
            """
            <div style='text-align: center;'>
                <h4>Enter your <a href="https://aistudio.google.com/app/apikey" target="_blank">Google Gemini API key</a> to start chatting</h4>
            </div>
            """,
            unsafe_allow_html=True,
        )

    def prompt_form(self):
        """
        Displays the prompt form and checks whether the form is ready
        """
        with st.form(key="my_form", clear_on_submit=True):
            user_input = st.text_area(
                "Query:",
                placeholder="Ask me anything...",
                key="input",
                label_visibility="collapsed",
            )
            submit_button = st.form_submit_button(label="Send")
            
            is_ready = submit_button and user_input
