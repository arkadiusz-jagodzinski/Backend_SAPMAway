import os

import matplotlib.pyplot as plt
from joblib import dump
from joblib import load
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import make_pipeline
from wordcloud import WordCloud

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
    dump(clf, os.getcwd() + os.path.sep + 'res' + os.path.sep + 'mlp_clf')


def generate_word_cloud():
    """
    Funkcja generuje, zwraca i zapisuje do pliku /res/cloud.png chumrę głównych słów spamu.
    :return: obraz z chmurą słów spamu
    """
    wc = WordCloud(background_color="white", width=1000, height=1000, normalize_plurals=True).generate_from_frequencies(
        clf[0].vocabulary_)
    fig = plt.imshow(wc)
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)
    plt.savefig(os.path.sep + 'res' + os.path.sep + 'cloud.png', bbox_inches='tight')
    return fig
