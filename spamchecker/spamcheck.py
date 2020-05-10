import os

from joblib import dump
from joblib import load
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import make_pipeline

clf = load(os.getcwd() + "/res/mlp_clf")


def isSpam(text):
    return clf.predict_proba([text])[0, 1]


def retrain_and_save_model(spam_data):
    """
    Trenuje model od zera na podstawie danych z bazy, następnie zapisuje wagi do folderu /res/. Nie wymaga przeładowania zapisanego modelu.
    :param spam_data: Tablica numpy, taka że w pierwszej kolumnie są teksty kolejnych smsów, a w drugiej wartość bool oznaczająca czy dany SMS jest spamem.
    :type spam_data: numpy array
    :return:
    """
    clf = make_pipeline(TfidfVectorizer("english"),
                        MLPClassifier(activation='logistic', hidden_layer_sizes=10, learning_rate='constant',
                                      solver='adam'))
    clf.fit(spam_data[0, :], spam_data[1, :])
    dump(clf, os.getcwd() + '/res/mlp_clf')
