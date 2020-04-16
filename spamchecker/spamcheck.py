from joblib import load

clf = load("..\\res\\mlp_clf")


def isSpam(text):
    return clf.predict_proba([text])[0, 1]
