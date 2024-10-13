import nltk
from nltk.tokenize import word_tokenize

# Download the necessary tokenizer models
nltk.download('all', force=True)

# Example text
text = "Natural Language Processing with Python is fun!"

# Tokenize the text into words
tokens = word_tokenize(text)

print(tokens)

