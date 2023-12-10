from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import string

def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    translator = str.maketrans('', '', string.punctuation)
    stemmer = PorterStemmer()

    words = word_tokenize(text.lower())
    words = [word.translate(translator) for word in words if word.isalnum()]
    words = [stemmer.stem(word) for word in words if word not in stop_words]

    return words

def build_inverted_index(books):
    inverted_index = {}

    for book in books:
        words = preprocess_text(get_book_content(book['url']))
        for word in set(words):
            if word not in inverted_index:
                inverted_index[word] = []
            inverted_index[word].append(book['title'])

    return inverted_index
