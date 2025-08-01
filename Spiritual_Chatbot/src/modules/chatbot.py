import streamlit as st
import google.generativeai as genai

class Chatbot:
    def __init__(self, api_key, model_name="gemini", temperature=0.5, vectors=None):
        # Configure Gemini API with the provided API key
        genai.configure(api_key=api_key)
        self.model_name = model_name
        self.temperature = temperature
        self.vectors = vectors  # If you're using vectors, you can handle them as needed.

    qa_template = """
        You are a helpful AI assistant named GitaGPT.
        If you don't know the answer, just say you don't know. Do NOT try to make up an answer.
        If the question is not related to the context, politely respond that you are tuned to only answer questions that are related to the context.
        Use as much detail as possible when responding.

        context: {context}
        =========
        question: {question}
        ======
        """

    def conversational_chat(self, query):
        """
        Start a conversational chat using the Google Gemini API
        """
        if not query:
            return "Please ask a valid question."

        # Assume that the vectors represent the context you're extracting from CSV or any documents
        context = self.get_context_from_vectors()

        # Compose the full prompt with context and query
        prompt = self.qa_template.format(context=context, question=query)

        # Call the Gemini chat API
        response = genai.chat(messages=[prompt])

        # Extract the response content
        answer = response["content"]

        # Append the query and answer to the conversation history
        st.session_state["history"].append((query, answer))

        return answer

    def get_context_from_vectors(self):
        """
        Helper function to retrieve context from vectors.
        This method assumes you are using the document embeddings (vectors) stored earlier.
        """
        if self.vectors:
            # If you're using document embeddings, extract context from them.
            context = " ".join([str(doc) for doc in self.vectors])  # Simplified context extraction from vectors
        else:
            context = "No context available."
        return context

