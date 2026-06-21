# 🤖 FAQ Chatbot (NLP-Based)

## 📌 Project Overview
This project is an **FAQ Chatbot** built using Python and Streamlit.  
It uses **Natural Language Processing (NLP)** techniques to understand user queries and return the most relevant answers from a predefined FAQ dataset.

The chatbot matches user questions using **TF-IDF Vectorization** and **Cosine Similarity**, making responses more intelligent compared to simple rule-based systems.

---

## 🚀 Features
- Interactive chatbot interface using Streamlit
- NLP-based question processing
- FAQ matching using cosine similarity
- Smart response selection
- Handles unknown queries gracefully

---

## 🛠️ Tech Stack
- Python
- Streamlit
- NLTK
- Scikit-learn
- NumPy

---

## 🧠 How It Works
1. FAQs are stored as question-answer pairs
2. Questions are converted into numerical vectors using TF-IDF
3. User input is also vectorized
4. Cosine similarity is used to find the closest match
5. Best matching answer is displayed

---

## 📂 Project Structure