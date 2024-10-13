import nltk
from nltk.stem import WordNetLemmatizer

# Download necessary NLTK data
#nltk.download('wordnet')
#nltk.download('omw-1.4')  # For wordnet language data (like synonyms)
#nltk.download('punkt')

# Initialize the WordNet Lemmatizer
lemmatizer = WordNetLemmatizer()

# Example words to lemmatize
words = ['running', 'ran', 'easily', 'fairly', 'faster']

# Lemmatize each word (assuming they are verbs)
lemmatized_words = [lemmatizer.lemmatize(word) for word in words]

# Print the original words and their lemmatized versions
for word, lemmatized in zip(words, lemmatized_words):
    print(f"Original: {word}, Lemma: {lemmatized}")

