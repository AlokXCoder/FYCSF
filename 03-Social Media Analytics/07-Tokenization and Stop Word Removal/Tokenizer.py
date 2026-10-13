import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords

# Download required NLTK data
nltk.download('punkt')
nltk.download('stopwords')

text = "This is a very useful cloud computing course."

tokens = word_tokenize(text)
stop_words = set(stopwords.words('english'))

filtered = [
    word for word in tokens
    if word.lower() not in stop_words
]

print(f"Tokens: {tokens}")
print(f"After Stopword Removal: {filtered}")