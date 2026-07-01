import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer


class TextVectorizer:
    def __init__(self):
        self.corpus = pd.read_csv("data/movies.csv")
        self.tfidf = TfidfVectorizer(stop_words="english", max_features=5000)
        self.matrix = None

    def fit(self):
        combined = (
            self.corpus["genre"] + " "
            + self.corpus["description"]
        )
        self.matrix = self.tfidf.fit_transform(combined)

    def get_corpus(self):
        return self.corpus

    def get_matrix(self):
        return self.matrix

    def get_tfidf(self):
        return self.tfidf
