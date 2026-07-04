from sklearn.metrics.pairwise import cosine_similarity

from engine.vectorizer import TextVectorizer


class Recommender:
    def __init__(self, vectorizer: TextVectorizer):
        self.vectorizer = vectorizer

    def _compute_hybrid_scores(self, query_vec, genre_query_vec, top_n):
        content_scores = cosine_similarity(query_vec, self.vectorizer.get_matrix()).flatten()
        genre_scores = cosine_similarity(genre_query_vec, self.vectorizer.get_genre_matrix()).flatten()
        hybrid = 0.7 * content_scores + 0.3 * genre_scores
        top_indices = hybrid.argsort()[::-1][:top_n]
        return content_scores, genre_scores, hybrid, top_indices

    def _get_matched_keywords(self, query, movie_idx, top_k=3):
        query_vec = self.vectorizer.get_tfidf().transform([query])
        feature_names = self.vectorizer.get_tfidf().get_feature_names_out()
        query_weights = query_vec.toarray().flatten()
        top_query_idx = query_weights.argsort()[::-1][:10]
        movie_weights = self.vectorizer.get_matrix()[movie_idx].toarray().flatten()
        matched = [feature_names[i] for i in top_query_idx if movie_weights[i] > 0]
        return matched[:top_k]

    def recommend(self, user_query: str, top_n: int = 5) -> list[dict]:
        query_vec = self.vectorizer.get_tfidf().transform([user_query])
        genre_query_vec = self.vectorizer.get_genre_tfidf().transform([user_query])
        content_scores, genre_scores, hybrid, top_indices = self._compute_hybrid_scores(
            query_vec, genre_query_vec, top_n
        )

        results = []
        for rank, idx in enumerate(top_indices, 1):
            row = self.vectorizer.get_corpus().iloc[idx]
            keywords = self._get_matched_keywords(user_query, idx)
            results.append({
                "rank": rank,
                "title": row["title"],
                "genre": row["genre"],
                "score": round(float(hybrid[idx]), 4),
                "content_score": round(float(content_scores[idx]), 4),
                "genre_score": round(float(genre_scores[idx]), 4),
                "keywords": keywords,
            })
        return results

    def recommend_similar(self, movie_title: str, top_n: int = 5) -> list[dict]:
        corpus = self.vectorizer.get_corpus()
        match = corpus[corpus["title"] == movie_title]
        if match.empty:
            return []
        idx = match.index[0]
        content_scores = cosine_similarity(
            self.vectorizer.get_matrix()[idx],
            self.vectorizer.get_matrix(),
        ).flatten()
        genre_scores = cosine_similarity(
            self.vectorizer.get_genre_matrix()[idx],
            self.vectorizer.get_genre_matrix(),
        ).flatten()
        content_scores[idx] = -1
        genre_scores[idx] = -1
        hybrid = 0.7 * content_scores + 0.3 * genre_scores
        top_indices = hybrid.argsort()[::-1][:top_n]

        source_row = match.iloc[0]
        source_text = source_row["genre"] + " " + source_row["description"]

        results = []
        for rank, midx in enumerate(top_indices, 1):
            row = corpus.iloc[midx]
            keywords = self._get_matched_keywords(source_text, midx)
            results.append({
                "rank": rank,
                "title": row["title"],
                "genre": row["genre"],
                "score": round(float(hybrid[midx]), 4),
                "content_score": round(float(content_scores[midx]), 4),
                "genre_score": round(float(genre_scores[midx]), 4),
                "keywords": keywords,
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
