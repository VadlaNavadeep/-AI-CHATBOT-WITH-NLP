
import nltk
import random
import string

# Ensure the 'punkt' tokenizer is available
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

# List of words that are considered greetings
greetings = ['hello', 'hi', 'hey', 'greetings']

# Possible responses for greetings
greeting_responses = ['Hello!', 'Hi there!', 'Greetings!', 'Hey!']

# Dictionary containing frequently asked questions and their responses
faq_data = {
    "what is your name": "I am a chatbot.",
    "how are you": "I'm doing well, thank you!",
    "what can you do": "I can answer your queries using NLP.",
    "what is nlp": "NLP stands for Natural Language Processing, a field of AI that deals with human language.",
    "what is python": "Python is a high-level, interpreted programming language known for its readability and simplicity.",
    "what is an internship": "An internship is a short-term work experience that allows students to gain practical skills in a specific field.",
    "what is your purpose": "I'm here to help you complete your internship tasks and answer basic questions.",
    "what is github": "GitHub is an online platform to host and share code using Git version control.",
    "what is machine learning": "Machine learning is a branch of AI that enables systems to learn from data and improve over time.",
    "can you help me": "Of course! Ask me any question related to Python, the internship, or general concepts.",
    "bye": "Goodbye! Have a nice day!",
}

# Function to find the best matching FAQ question using edit distance
def find_best_match(user_input):
    min_distance = float('inf')
    best_match = None

    for question in faq_data:
        distance = nltk.edit_distance(user_input, question)
        if distance < min_distance:
            min_distance = distance
            best_match = question

    if min_distance < 10:
        return faq_data[best_match]
    return None

# Function to process the user's input and return an appropriate response
def get_response(user_input):
    user_input = user_input.lower()
    tokens = nltk.word_tokenize(user_input)

    # Normalize and check for greetings
    for word in tokens:
        word_clean = word.strip(string.punctuation)
        if word_clean in greetings:
            return random.choice(greeting_responses)

    answer = find_best_match(user_input)
    if answer:
        return answer

    return "I'm not sure I understand. Could you try asking something else?"

# Start of the chatbot interaction loop
print("Chatbot: Hello! Ask me anything. Type 'bye', 'exit', or 'quit' to leave.")

while True:
    user_input = input("You: ").strip()

    if user_input.lower() in ['bye', 'exit', 'quit']:
        print("Chatbot:", faq_data["bye"])
        break

    print("Chatbot:", get_response(user_input))
