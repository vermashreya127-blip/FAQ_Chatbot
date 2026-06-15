import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="FAQ Chatbot",
    page_icon="🤖",
    layout="centered"
)

# Title
st.title("🤖 FAQ Chatbot")
st.write("### Ask me a question!")

# Input
question = st.text_input("Enter your question:")

# FAQ Logic
if question:
    question = question.lower()

    if "hello" in question or "hi" in question:
        st.success("Hello! How can I help you today? 😊")

    elif "your name" in question:
        st.success("I am an AI FAQ Chatbot.")

    elif "python" in question:
        st.success(
            "Python is a popular programming language used for web development, AI, automation, and data science."
        )

    elif "streamlit" in question:
        st.success(
            "Streamlit is a Python framework used to build interactive web applications quickly."
        )

    elif "ai" in question or "artificial intelligence" in question:
        st.success(
            "Artificial Intelligence enables machines to perform tasks that normally require human intelligence."
        )

    elif "machine learning" in question:
        st.success(
            "Machine Learning is a branch of AI where computers learn patterns from data without being explicitly programmed."
        )

    elif "data science" in question:
        st.success(
            "Data Science involves collecting, analyzing, and visualizing data to gain useful insights."
        )

    elif "bye" in question:
        st.success("Goodbye! Have a great day. 👋")

    else:
        st.warning("Sorry, I don't know the answer to that question.")