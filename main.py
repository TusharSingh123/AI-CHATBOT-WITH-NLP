import warnings
warnings.filterwarnings("ignore", category=UserWarning)

import nltk
import numpy as np
import random
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# File path containing the chatbot training data
FILE_PATH = 'data.txt'

# Read and preprocess the text data
with open(FILE_PATH, 'r', errors='ignore') as f:
    raw = f.read().lower()

# Download required NLTK resources
nltk.download('punkt')
nltk.download('wordnet')

# Tokenize into sentences and words
sentence_tokens = nltk.sent_tokenize(raw)
word_tokens = nltk.word_tokenize(raw)

# Initialize lemmatizer and punctuation removal dictionary
lemmer = nltk.stem.WordNetLemmatizer()
remove_punct_dict = dict((ord(p), None) for p in string.punctuation)

# Lemmatize tokens
def lem_tokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]

# Normalize text by removing punctuation and lemmatizing
def lem_normalize(text):
    return lem_tokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

# Expanded list of greeting inputs and responses
GREETING_INPUTS = (
    'hello', 'hi', 'greetings', 'sup', 'what\'s up', 'hey', 'yo', 'howdy',
    'hola', 'namaste', 'good morning', 'good evening', 'good afternoon'
)
GREETING_RESPONSES = [
    'Hi there!', 'Hey!', 'Hello!', '*nods*', 'Greetings!', 'Howdy!',
    'Namaste!', 'Hi! Glad to see you.', 'Hey buddy!', 'Yo! What’s up?'
]

# Return a greeting if user input contains a greeting word
def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

# Generate chatbot response using TF-IDF and cosine similarity
def response(user_response):
    robo_response = ''
    sentence_tokens.append(user_response)
    
    vectorizer = TfidfVectorizer(tokenizer=lem_normalize, stop_words='english')
    tfidf = vectorizer.fit_transform(sentence_tokens)
    
    values = cosine_similarity(tfidf[-1], tfidf)
    idx = values.argsort()[0][-2]
    flat = values.flatten()
    flat.sort()
    req_tfidf = flat[-2]

    if req_tfidf == 0:
        robo_response = "Sorry, I don't understand you."
    else:
        robo_response = sentence_tokens[idx]
    
    sentence_tokens.remove(user_response)
    return robo_response

# Main interaction loop
print("BOT: My name is Robo. I can answer your questions about chatbots. Type 'bye' to exit.")

while True:
    user_response = input("YOU: ").lower()

    if user_response == 'bye':
        print("BOT: Bye! Have a nice day.")
        break
    elif user_response in ['thanks', 'thank you']:
        print("BOT: You're welcome!")
        break
    elif greeting(user_response) is not None:
        print(f"BOT: {greeting(user_response)}")
    else:
        print(f"BOT: {response(user_response)}")
