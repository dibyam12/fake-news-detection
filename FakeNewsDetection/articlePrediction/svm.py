
import numpy as np
import pandas as pd
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

# def Svm(text):
#     # Importing dataset for true and fake news
#     true_data = pd.read_csv(r'C:\Users\user\Desktop\Fake-News-Detection-UsingMachineLearning1\Fake-News-Detection-UsingMachineLearning\Fake-News-Detection-UsingMachineLearning-master\FakeNewsDetection\processedTrue.csv')  # Adjust the correct path
#     fake_data = pd.read_csv(r'C:\Users\user\Desktop\Fake-News-Detection-UsingMachineLearning1\Fake-News-Detection-UsingMachineLearning\Fake-News-Detection-UsingMachineLearning-master\FakeNewsDetection\processedFake.csv')  # Adjust the correct path

#     # Concatenate the two datasets
#     data = pd.concat([true_data, fake_data], ignore_index=True, sort=False)

#     # Setting column names
#     data.columns = ['index', 'label', 'content']

#     # Features and labels
#     X = data['content']
#     y = data['label']

#     # Train-test split
#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, shuffle=True, random_state=1)

#     # TF-IDF vectorizer (fitted on the training data)
#     tfidf_vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)

#     # Fit the vectorizer on training data and transform the data
#     X_train = tfidf_vectorizer.fit_transform(X_train) 
#     X_test = tfidf_vectorizer.transform(X_test)

#     # Save the TF-IDF vectorizer for later use during prediction
#     with open(r'C:\Users\user\Desktop\Fake-News-Detection-UsingMachineLearning1\Fake-News-Detection-UsingMachineLearning\Fake-News-Detection-UsingMachineLearning-master\FakeNewsDetection\models\tfidf_vectorizer.pkl', 'wb') as vectorizer_file:
#         pickle.dump(tfidf_vectorizer, vectorizer_file)

#     # Load the pre-trained SVM model
#     with open(r'C:\Users\user\Desktop\Fake-News-Detection-UsingMachineLearning1\Fake-News-Detection-UsingMachineLearning\Fake-News-Detection-UsingMachineLearning-master\FakeNewsDetection\models\model.pkl', 'rb') as model_file:
#         SVM_Model = pickle.load(model_file)

#     # Transform the input text using the same TF-IDF vectorizer
#     news = [text]  # Wrap the text in a list
#     news_transformed = tfidf_vectorizer.transform(news)  # Use the same vectorizer

#     # Predict using the trained model
#     value = SVM_Model.predict(news_transformed)

#     # Return the prediction result
#     if value == 1:
#         return 'FAKE'
#     else:
#         return 'REAL'


def Svm(text):
    #Importing dataset
    true_data = pd.read_csv(r'C:\Users\user\Desktop\Fake-News-Detection-UsingMachineLearning1\Fake-News-Detection-UsingMachineLearning\Fake-News-Detection-UsingMachineLearning-master\FakeNewsDetection\processedTrue.csv')
    fake_data = pd.read_csv(r'C:\Users\user\Desktop\Fake-News-Detection-UsingMachineLearning1\Fake-News-Detection-UsingMachineLearning\Fake-News-Detection-UsingMachineLearning-master\FakeNewsDetection\processedFake.csv')

    data = pd.concat( [true_data, fake_data], ignore_index=True, sort=False)

    data.columns = ['index', 'label', 'content']

    X = data['content']
    y = data['label']


    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, shuffle=True, random_state=1)


    
    # import pickle

    with open(r'C:\Users\user\Desktop\Fake-News-Detection-UsingMachineLearning1\Fake-News-Detection-UsingMachineLearning\Fake-News-Detection-UsingMachineLearning-master\FakeNewsDetection\models\model.pkl', 'rb') as file:
        SVM_Model = pickle.load(file)

    tfidf_vectorizer=TfidfVectorizer(stop_words='english', max_df=0.7)
    X_train=tfidf_vectorizer.fit_transform(X_train) 
    X_test=tfidf_vectorizer.transform(X_test)

    # news = ["budget fight loom reuters head flip fiscal script conservative republican faction u congress republicans washington"]
    
    news = []
    news.append(text)
    news = tfidf_vectorizer.transform(news)

    value = SVM_Model.predict(news)

    if value == 1:
        return('FAKE')
    else:
        return('REAL')
