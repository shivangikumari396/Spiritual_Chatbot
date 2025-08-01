import streamlit as st

class Sidebar:

    MODEL_OPTIONS = ["gpt-3.5-turbo", "gpt-4"]
    TEMPERATURE_MIN_VALUE = 0.0
    TEMPERATURE_MAX_VALUE = 1.0
    TEMPERATURE_DEFAULT_VALUE = 0.0
    TEMPERATURE_STEP = 0.01

    @staticmethod
    def about():
        about = st.sidebar.expander("🧠 About this Bot ")
        sections = [
            "#### It is an AI chatbot with a conversational memory, designed to allow users to discuss their queries related to spiritual texts in a more intuitive way. 📄",
            "#### It uses large language models to provide users with natural language interactions about Spiritual Texts. 🌐",
            "#### Powered by [Langchain](https://github.com/hwchase17/langchain) and [Streamlit](https://github.com/streamlit/streamlit) ⚡",
        ]
        for section in sections:
            about.write(section)

    @staticmethod
    def reset_chat_button():
        # Set default for reset_chat first, then check button state
        st.session_state.setdefault("reset_chat", False)
        if st.button("Reset chat"):
            st.session_state["reset_chat"] = True

    def model_selector(self):
        st.session_state.setdefault("model", self.MODEL_OPTIONS[0])
        model = st.selectbox(label="Model", options=self.MODEL_OPTIONS)
        st.session_state["model"] = model

    def temperature_slider(self):
        st.session_state.setdefault("temperature", self.TEMPERATURE_DEFAULT_VALUE)
        temperature = st.slider(
            label="Temperature",
            min_value=self.TEMPERATURE_MIN_VALUE,
            max_value=self.TEMPERATURE_MAX_VALUE,
            value=st.session_state["temperature"],  # Set to session state value
            step=self.TEMPERATURE_STEP,
        )
        st.session_state["temperature"] = temperature

    def show_options(self):
        with st.sidebar.expander("🛠️ Tools", expanded=False):
            # Ensure defaults are set before displaying options
            self.reset_chat_button()
            self.model_selector()
            self.temperature_slider()
            st.session_state.setdefault("model", self.MODEL_OPTIONS[0])
            st.session_state.setdefault("temperature", self.TEMPERATURE_DEFAULT_VALUE)

    