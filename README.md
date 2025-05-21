# -AI-CHATBOT-WITH-NLP

COMPANY: CODTECH IT SOLUTIONS

NAME: Vadla Navadeep

INTERN ID: CT04DM1346

DOMAIN: Python Programming

DURATION: 4 Weeks

MENTOR: NEELA SANTOSH

# 🤖 NLP-Based Chatbot using Python & NLTK

## 📄 Overview

This is a **rule-based chatbot** built with **Python** and the **Natural Language Toolkit (NLTK)**. It uses basic NLP techniques to process user input and responds with relevant answers from a predefined FAQ knowledge base.

The chatbot:
- Recognizes greetings
- Matches queries using **edit distance**
- Responds with fallback messages for unknown inputs

This project is perfect for learning how to implement NLP concepts in a chatbot without diving into machine learning.

---

## ✨ Features

- 🧠 **Natural Language Processing**  
  Tokenizes and analyzes user input using NLTK

- 💬 **Predefined Knowledge Base**  
  Answers FAQs about Python, machine learning, GitHub, internships, etc.

- 🔁 **Continuous Chat Loop**  
  Keeps the conversation going until the user says `bye`, `exit`, or `quit`

- 👋 **Greeting Detection**  
  Recognizes and responds to basic greetings like "hello" and "hi"

- 🎯 **Edit Distance Matching**  
  Matches queries with slight spelling variations using edit distance

- ❓ **Fallback Handling**  
  Requests clarification when it doesn’t understand the query

---

## 🛠 Technologies Used

- **Python** – Programming language  
- **NLTK** – Natural Language Toolkit for tokenization and similarity checking  

> ✅ No APIs, databases, or third-party frameworks used. It's lightweight and runs entirely in the terminal.

---

## 📁 Project Structure

chatbot_project/
│
├── chatbot.py # Main chatbot script
└── README.md # Project documentation

1. 🔧 Prerequisites

Ensure Python 3.x is installed:

```bash
python --version


2. 📦 Install Dependencies
Install the required package:
pip install nltk

3. 📂 Download NLTK Resources
These resources will be downloaded automatically on first run, but you can also do it manually:

python
Copy
Edit
import nltk
nltk.download('punkt')
4. 🚀 Run the Chatbot
Run the chatbot script from your terminal:

bash
Copy
Edit
python chatbot.py
5. 💬 Interact with the Bot
Example:

vbnet
Copy
Edit
You: Hello
Chatbot: Hi there!

You: What is Python?
Chatbot: Python is a high-level, interpreted programming language...
6. ❌ Exit the Chat
Type any of the following to end the conversation:

bash
Copy
Edit
bye
exit
quit
📌 Note
This chatbot is for educational and demonstration purposes only. You can expand it by:

Adding a GUI

Using APIs for dynamic responses

Implementing machine learning models for better accuracy

The goal here is to focus on core NLP logic using NLTK in the simplest way possible.
