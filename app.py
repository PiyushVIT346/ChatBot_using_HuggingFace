import streamlit as st
from transformers import pipeline

# Load the text generation pipeline with BlenderBot model
chatbot_model = pipeline("text-generation", model="facebook/blenderbot-400M-distill")

# Chat history to maintain conversation context
chat_history = []

# Function to get chatbot response
def get_response(user_input):
    # Append user input to chat history for context
    chat_history.append(f"User: {user_input}")
    
    # Use the text generation pipeline to generate a response
    response = chatbot_model(f"{' '.join(chat_history)} Bot: ", max_length=100, num_return_sequences=1)
    
    # Extract generated text and append it to chat history
    bot_reply = response[0]['generated_text'].split("Bot: ")[-1].strip()
    chat_history.append(f"Bot: {bot_reply}")
    
    return bot_reply

# Streamlit interface
st.title("NLP Chatbot using Hugging Face Transformers")

# Capture user input
user_input = st.text_input("You: ", "Hello! How are you?")

# If user submits input, get the chatbot's response
if user_input:
    response = get_response(user_input)
    st.text_area("Chatbot: ", value=response, height=100)
