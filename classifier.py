import joblib


class Classifier(object):
    def __init__(self):
        self.vectorizer = joblib.load("fake_news_vectorizer_dump.pkl")
        self.model = joblib.load("fake_news_model_dump.pkl")
        self.target = ['is_fake']

    def predict_probas(self, text):
        vectorized = self.vectorizer.transform([text])
        return self.model.predict_proba(vectorized)

    def get_result(self, text):
        predictions = self.predict_probas(text)
        return predictions[0]