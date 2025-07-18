# AI-CHATBOT-WITH-NLP

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: TUSHAR SINGH

*INTERN ID*: CT06DG16

*DOMAIN*: PYTHON PROGRAMMING

*DURATION*: 6 WEEKS

*MENTOR*: NEELA SANTOSH
</br>
</br>
</br>
![Chatbot Output]([https://github-production-user-asset-6210df.s3.amazonaws.com/152875478/468131667-9a59347a-fdb7-4f26-b1eb-e552f064aff9.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20250718%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20250718T165237Z&X-Amz-Expires=300&X-Amz-Signature=00f0d1e96790d2a9c63a1a20d9e765e8d223dc1be241e35dd8c32ffc77d9df38&X-Amz-SignedHeaders=host](https://github.com/user-attachments/assets/cecc6894-618d-41c2-a579-7516e0d26f82))
*A sample conversation with the chatbot showing user input and responses.*

</br>
</br>
</br>
# Intelligent Chatbot with TF-IDF and Cosine Similarity

A sophisticated conversational AI chatbot built using Python, NLTK, and scikit-learn that employs TF-IDF vectorization and cosine similarity for intelligent response generation. This chatbot can engage in natural conversations by analyzing text patterns and finding the most relevant responses from its training data.

## Features

- **Natural Language Processing**: Utilizes NLTK for text tokenization, lemmatization, and preprocessing
- **TF-IDF Vectorization**: Implements Term Frequency-Inverse Document Frequency for text analysis
- **Cosine Similarity**: Measures text similarity to find the most relevant responses
- **Greeting Recognition**: Intelligent greeting detection with varied responses
- **Text Normalization**: Removes punctuation and normalizes text for better processing
- **Expandable Knowledge Base**: Easy to update with new training data
- **Interactive Console Interface**: Simple command-line interaction

## Technology Stack

- **Python 3.x**: Core programming language
- **NLTK**: Natural Language Toolkit for text processing
- **scikit-learn**: Machine learning library for TF-IDF and similarity calculations
- **NumPy**: Numerical computing support

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/AI-CHATBOT-WITH-NLP.git
   cd AI-CHATBOT-WITH-NLP
   ```

2. **Install required dependencies:**
   ```bash
   pip install nltk scikit-learn numpy
   ```

3. **Download NLTK data:**
   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('wordnet')
   ```

## Usage

1. **Prepare your training data:**
   - Create a `data.txt` file in the project directory
   - Add your training text data (conversations, FAQs, knowledge base content)
   - The more diverse and comprehensive your data, the better the chatbot's responses

2. **Run the chatbot:**
   ```bash
   python main.py
   ```

3. **Interact with the bot:**
   - Type your messages and press Enter
   - The bot will respond based on its training data
   - Type 'bye' to exit the conversation
   - Type 'thanks' or 'thank you' to end with gratitude

## How It Works

### Text Processing Pipeline

1. **Data Preprocessing**: The chatbot reads and preprocesses the training data by converting to lowercase and tokenizing into sentences
2. **Lemmatization**: Words are reduced to their root forms using WordNet lemmatizer
3. **Punctuation Removal**: Special characters and punctuation are stripped from the text
4. **TF-IDF Vectorization**: Text is converted into numerical vectors representing word importance
5. **Similarity Calculation**: Cosine similarity determines the most relevant response from the training data

### Response Generation

The chatbot uses a sophisticated algorithm to generate responses:

- **Greeting Detection**: Recognizes various greeting patterns and responds appropriately
- **Context Matching**: Finds the most similar sentence in the training data using cosine similarity
- **Fallback Handling**: Provides a default response when no suitable match is found

## Project Structure

```
AI-CHATBOT-WITH-NLP/
│
├── chatbot.py          # Main chatbot implementation
├── data.txt            # Training data file
├── README.md          # Project documentation
└── requirements.txt   # Python dependencies
```

## Customization

### Adding New Greetings

Expand the greeting functionality by modifying the `GREETING_INPUTS` and `GREETING_RESPONSES` lists:

```python
GREETING_INPUTS = (
    'hello', 'hi', 'greetings', 'sup', 'what\'s up', 'hey', 'yo', 'howdy',
    'hola', 'namaste', 'good morning', 'good evening', 'good afternoon',
    # Add your custom greetings here
)
```

### Improving Training Data

For better responses, structure your `data.txt` file with:
- Frequently asked questions and answers
- Common conversation patterns
- Domain-specific knowledge
- Varied sentence structures and vocabulary

## Example Conversations

```
BOT: My name is Robo. I can answer your questions about chatbots. Type 'bye' to exit.
YOU: hello
BOT: Hi there!
YOU: what is chatbot?
BOT: [Response based on training data about machine learning]
YOU: thanks
BOT: You're welcome!
```

## Performance Considerations

- **Training Data Size**: Larger datasets provide more diverse responses but increase processing time
- **Memory Usage**: TF-IDF vectors are stored in memory; consider optimization for large datasets
- **Response Time**: Similarity calculations are performed in real-time for each user input

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Acknowledgments

- NLTK team for the natural language processing toolkit
- scikit-learn contributors for machine learning algorithms
- Python community for the robust ecosystem
---

*Built with ❤️ using Python and Natural Language Processing*
