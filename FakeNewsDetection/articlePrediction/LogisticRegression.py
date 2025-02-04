import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pickle

class LogisticRegression:
    def __init__(self, learning_rate=0.01, iterations=100, batch_size=32):
        self.learning_rate = learning_rate
        self.iterations = iterations
        self.batch_size = batch_size

    def fit(self, X, y):
        self.m, self.n = X.shape
        self.weights = np.zeros(self.n)
        self.bias = 0

        for _ in range(self.iterations):
            indices = np.random.permutation(self.m)
            X_shuffled = X[indices]
            y_shuffled = y[indices]

            for i in range(0, self.m, self.batch_size):
                X_batch = X_shuffled[i:i+self.batch_size]
                y_batch = y_shuffled[i:i+self.batch_size]

                z = X_batch.dot(self.weights) + self.bias
                predictions = self.sigmoid(z)

                error = y_batch - predictions
                gradient_weights = X_batch.T.dot(error) / self.batch_size
                gradient_bias = np.sum(error) / self.batch_size

                self.weights += self.learning_rate * gradient_weights
                self.bias += self.learning_rate * gradient_bias

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def predict(self, X):
        z = X.dot(self.weights) + self.bias
        return np.round(self.sigmoid(z)).astype(int)

def lr_predict(text):
    # Load datasets
    true_data = pd.read_csv(r'C:/Users/user/Desktop/Fake-News-Detection-UsingMachineLearning1/Fake-News-Detection-UsingMachineLearning/Fake-News-Detection-UsingMachineLearning-master/FakeNewsDetection/processedTrue.csv')
    fake_data = pd.read_csv(r'C:/Users/user/Desktop/Fake-News-Detection-UsingMachineLearning1/Fake-News-Detection-UsingMachineLearning/Fake-News-Detection-UsingMachineLearning-master/FakeNewsDetection/processedFake.csv')

    data = pd.concat([true_data, fake_data], ignore_index=True, sort=False)
    data.columns = ['index', 'label', 'content']

    X = data['content']
    y = data['label']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, shuffle=True, random_state=1)

    # TF-IDF Vectorizer
    tfidf_vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
    X_train = tfidf_vectorizer.fit_transform(X_train)
    X_test = tfidf_vectorizer.transform(X_test)

    # Save the vectorizer
    with open(r'C:/Users/user/Desktop/Fake-News-Detection-UsingMachineLearning1/Fake-News-Detection-UsingMachineLearning/Fake-News-Detection-UsingMachineLearning-master/FakeNewsDetection/models/tfidf_vectorizer.pkl', 'wb') as vectorizer_file:
        pickle.dump(tfidf_vectorizer, vectorizer_file)

    # Load or train the Logistic Regression model
    model_path = r'C:/Users/user/Desktop/Fake-News-Detection-UsingMachineLearning1/Fake-News-Detection-UsingMachineLearning/Fake-News-Detection-UsingMachineLearning-master/FakeNewsDetection/models/lr_model.pkl'

    try:
        with open(model_path, 'rb') as model_file:
            lr_model = pickle.load(model_file)
    except FileNotFoundError:
        lr_model = LogisticRegression(learning_rate=0.01, iterations=100, batch_size=32)
        lr_model.fit(X_train, y_train.to_numpy())
        with open(model_path, 'wb') as model_file:
            pickle.dump(lr_model, model_file)

    # Transform the input text and predict
    news = tfidf_vectorizer.transform([text])
    prediction = lr_model.predict(news)

    return 'FAKE' if prediction[0] == 1 else 'REAL'
