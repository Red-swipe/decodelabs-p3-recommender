import streamlit as st

from engine.vectorizer import TextVectorizer
from engine.recommender import Recommender


st.set_page_config(page_title="Movie Recommendation Engine", layout="wide")

@st.cache_resource
def load_engine():
    v = TextVectorizer()
    v.fit()
    return v, Recommender(v)


vectorizer, recommender = load_engine()
corpus = vectorizer.get_corpus()
all_genres = sorted(corpus["genre"].unique())

if "history" not in st.session_state:
    st.session_state.history = []
if "last_query" not in st.session_state:
    st.session_state.last_query = None
if "last_results" not in st.session_state:
    st.session_state.last_results = []
if "similar_source" not in st.session_state:
    st.session_state.similar_source = None
if "similar_results" not in st.session_state:
    st.session_state.similar_results = []


with st.sidebar:
    st.header("Filters")
    selected_genres = st.multiselect("Filter by genre", all_genres, placeholder="All genres")

    st.markdown("---")
    st.markdown("##### IMDB Rating Filter")
    st.caption("IMDB ratings are not available in the current dataset. This filter will appear once rating data is added.")

    st.markdown("---")
    st.markdown("##### Search History")
    if st.session_state.history:
        for q in reversed(st.session_state.history[-5:]):
            st.markdown(f"- {q}")
        if st.button("Clear History"):
            st.session_state.history = []
            st.rerun()
    else:
        st.caption("No searches yet.")

st.title("Movie Recommendation Engine")
st.markdown("Content-Based Filtering using TF-IDF Similarity")

query = st.text_input("What are you in the mood for?", placeholder="e.g. space adventure, dark thriller, feel-good comedy")
top_n = st.slider("Number of recommendations", 1, 10, 5)

if st.button("Get Recommendations", type="primary") and query.strip():
    q = query.strip()
    if q not in st.session_state.history:
        st.session_state.history.append(q)
    st.session_state.last_query = q
    raw = recommender.recommend(q, top_n=20)
    if selected_genres:
        raw = [r for r in raw if r["genre"] in selected_genres]
    st.session_state.last_results = raw[:top_n]
    st.session_state.similar_source = None
    st.session_state.similar_results = []
    st.rerun()

if st.session_state.last_results:
    st.subheader(f"Results for \"{st.session_state.last_query}\"")
    ncols = 3
    for i in range(0, len(st.session_state.last_results), ncols):
        cols = st.columns(ncols)
        for j, rec in enumerate(st.session_state.last_results[i:i+ncols]):
            with cols[j]:
                with st.container(border=True):
                    st.markdown(f"##### {rec['title']}")
                    st.markdown(f"*{rec['genre']}* — Match: **{rec['score']*100:.1f}%**")
                    key = f"mlt_{i}_{j}_{rec['title']}"
                    if st.button("More like this", key=key):
                        st.session_state.similar_source = rec["title"]
                        st.session_state.similar_results = recommender.recommend_similar(rec["title"], top_n=5)
                        st.rerun()

if st.session_state.similar_results:
    st.markdown("---")
    st.subheader(f"More like \"{st.session_state.similar_source}\"")
    ncols = 3
    for i in range(0, len(st.session_state.similar_results), ncols):
        cols = st.columns(ncols)
        for j, sr in enumerate(st.session_state.similar_results[i:i+ncols]):
            with cols[j]:
                with st.container(border=True):
                    st.markdown(f"##### {sr['title']}")
                    st.markdown(f"*{sr['genre']}* — Match: **{sr['score']*100:.1f}%**")
