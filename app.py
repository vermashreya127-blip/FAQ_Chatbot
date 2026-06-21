import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
import numpy as np

nltk.download('punkt')

# FAQ dataset
faqs = {
    "What is AI?": "AI stands for Artificial Intelligence, which enables machines to think and learn like humans.",
    "What is Python?": "Python is a high-level programming language used for AI, web development, and data science.",
    "What is Streamlit?": "Streamlit is a Python library used to create web apps for data science and machine learning.",
    "What is machine learning?": "Machine learning is a branch of AI that allows systems to learn from data automatically."
}

questions = list(faqs.keys())
answers = list(faqs.values())

# Preprocess using TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(questions)

def get_response(user_input):
    user_vec = vectorizer.transform([user_input])
    similarity = cosine_similarity(user_vec, X)
    idx = np.argmax(similarity)

    # If similarity is too low
    if similarity[0][idx] < 0.3:
        return "Sorry, I don't understand your question. Please try again."

    return answers[idx]

# Streamlit UI
st.title("FAQ Chatbot 🤖")

user_input = st.text_input("Ask your question:")

if user_input:
    response = get_response(user_input)
    st.write("Bot:", response)