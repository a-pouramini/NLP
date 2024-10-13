import nltk
from nltk.stem import PorterStemmer

# Download necessary NLTK data
nltk.download('punkt')

# Initialize the Porter Stemmer
porter = PorterStemmer()

# Example words to stem
words = ['running', 'ran', 'easily', 'fairly', 'faster']

# Stem each word using the Porter Stemmer
stemmed_words = [porter.stem(word) for word in words]

# Print the original words and their stemmed versions
for word, stemmed in zip(words, stemmed_words):
    print(f"Original: {word}, Stemmed: {stemmed}")

