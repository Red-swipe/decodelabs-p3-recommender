import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer


class TextVectorizer:
    def __init__(self):
        self.corpus = pd.read_csv("data/movies.csv")
        self.tfidf = TfidfVectorizer(stop_words="english", max_features=5000)
        self.genre_tfidf = TfidfVectorizer(stop_words="english", max_features=500)
        self.matrix = None
        self.genre_matrix = None

    def fit(self):
        combined = (
            self.corpus["genre"] + " "
            + self.corpus["description"]
        )
        self.matrix = self.tfidf.fit_transform(combined)
        self.genre_matrix = self.genre_tfidf.fit_transform(self.corpus["genre"])

    def get_corpus(self):
        return self.corpus

    def get_matrix(self):
        return self.matrix

    def get_tfidf(self):
        return self.tfidf

    def get_genre_matrix(self):
        return self.genre_matrix

    def get_genre_tfidf(self):
        return self.genre_tfidf
