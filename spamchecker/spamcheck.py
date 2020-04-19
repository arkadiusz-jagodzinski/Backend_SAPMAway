from joblib import load
import os

clf = load(os.getcwd() + "/res/mlp_clf")

def isSpam(text):
    return clf.predict_proba([text])[0, 1]
