from sklearn.metrics.pairwise import cosine_similarity

from engine.vectorizer import TextVectorizer


class Recommender:
    def __init__(self, vectorizer: TextVectorizer):
        self.vectorizer = vectorizer

    def recommend(self, user_query: str, top_n: int = 5) -> list[dict]:
        query_vec = self.vectorizer.get_tfidf().transform([user_query])
        scores = cosine_similarity(query_vec, self.vectorizer.get_matrix()).flatten()
        top_indices = scores.argsort()[::-1][:top_n]

        results = []
        for rank, idx in enumerate(top_indices, 1):
            row = self.vectorizer.get_corpus().iloc[idx]
            results.append({
                "rank": rank,
                "title": row["title"],
                "genre": row["genre"],
                "score": round(float(scores[idx]), 4),
            })
        return results

    def recommend_similar(self, movie_title: str, top_n: int = 5) -> list[dict]:
        corpus = self.vectorizer.get_corpus()
        match = corpus[corpus["title"] == movie_title]
        if match.empty:
            return []
        idx = match.index[0]
        scores = cosine_similarity(
            self.vectorizer.get_matrix()[idx],
            self.vectorizer.get_matrix(),
        ).flatten()
        scores[idx] = -1
        top_indices = scores.argsort()[::-1][:top_n]

        results = []
        for rank, idx in enumerate(top_indices, 1):
            row = corpus.iloc[idx]
            results.append({
                "rank": rank,
                "title": row["title"],
                "genre": row["genre"],
                "score": round(float(scores[idx]), 4),
            })
        return results


if __name__ == "__main__":
    from engine.vectorizer import TextVectorizer

    v = TextVectorizer()
    v.fit()
    r = Recommender(v)
    results = r.recommend("space adventure with robots", top_n=3)
    for res in results:
        print(res)
