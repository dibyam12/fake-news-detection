# import numpy as np
# import pandas as pd
# import re
# import string
# from nltk.corpus import stopwords
# from sklearn.feature_extraction.text import TfidfVectorizer
# from nltk.stem import WordNetLemmatizer

# import nltk
# # nltk.download('stopwords')
# # nltk.download('punkt')
# # nltk.download('wordnet')

# stopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]

# word_lemma = WordNetLemmatizer()

# def cleanWord(text):
#     text = text.lower()
#     text = re.sub('\[.*?\]', '', text)
#     text = re.sub("\\W", " ", text)
#     text = re.sub('https?://\S+|www\.\S+', '', text)
#     text = re.sub('<.*?>+', '', text)
#     text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
#     text = re.sub('\n', '', text)
#     text = re.sub('\w*\d\w*', '', text)
#     text = re.sub('[^a-zA-Z]',' ',text)
#     text = text.split()
#     # text = [word_lemma.lemmatize(word, pos="v") for word in text if not word in stopwords]
#     text = ' '.join(text)
#     return text

import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Initialize lemmatizer and stop words
word_lemma = WordNetLemmatizer()
nltk.download('wordnet')
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

def cleanWord(text):
    """
    Cleans and preprocesses input text by removing unnecessary elements, punctuation, and stopwords.
    """
    try:
        # Lowercase and remove unwanted characters
        text = text.lower()
        text = re.sub(r'https?://\S+|www\.\S+', '', text)  # Remove URLs
        text = re.sub(r'<.*?>+', '', text)  # Remove HTML tags
        text = re.sub(r'[%s]' % re.escape(string.punctuation), '', text)  # Remove punctuation
        text = re.sub(r'\n', ' ', text)  # Replace newlines with space
        text = re.sub(r'\w*\d\w*', '', text)  # Remove words with numbers

        # Tokenization and stopword removal
        text = text.split()
        text = [word_lemma.lemmatize(word) for word in text if word not in stop_words]

        return ' '.join(text)
    except Exception as e:
        print(f"Error during text cleaning: {e}")
        return ""
