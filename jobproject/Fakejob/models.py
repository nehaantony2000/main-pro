from django.db import models

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from django.conf import settings

class FakeJobDetector:
    def __init__(self):
        self.tfidf_vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
        self.model = LogisticRegression()
        self.load_model()

    def load_model(self):
        model_path = settings.BASE_DIR / 'fake_job_detection' / 'model'
        self.tfidf_vectorizer = pd.read_pickle(model_path / 'tfidf_vectorizer.pkl')
        self.model = pd.read_pickle(model_path / 'model.pkl')

    def predict(self, text):
        text_tfidf = self.tfidf_vectorizer.transform([text])
        label = self.model.predict(text_tfidf)[0]
        return label