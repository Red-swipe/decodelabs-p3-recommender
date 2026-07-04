import streamlit as st

from engine.vectorizer import TextVectorizer
from engine.recommender import Recommender


st.set_page_config(page_title="Movie Recommendation Engine", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #0e1117; color: #e0e0e0; }
    .stTextInput input { background-color: #1e1e1e; color: #e0e0e0; }
    div[data-testid="stVerticalBlock"] > div { background-color: transparent !important; }
    .stButton button { background-color: #ff4b4b; color: white; border: none; }
    .stButton button:hover { background-color: #ff3333; }
    h1, h2, h3, h4, h5, h6 { color: #f0f0f0; }
    .stMarkdown { color: #d0d0d0; }
    .stSidebar { background-color: #1a1a2e; }
    .stSlider label { color: #d0d0d0; }
    .stMultiSelect label { color: #d0d0d0; }
    .stCaption { color: #a0a0a0; }
</style>
""", unsafe_allow_html=True)

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
if "history_click" not in st.session_state:
    st.session_state.history_click = None


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
            if st.button(f"🔍 {q}", key=f"hist_{q}"):
                st.session_state.history_click = q
                st.rerun()
        if st.button("Clear History"):
            st.session_state.history = []
            st.rerun()
    else:
        st.caption("No searches yet.")

st.title("Movie Recommendation Engine")
st.markdown("Content-Based Filtering using TF-IDF Similarity")

query = st.text_input("What are you in the mood for?", placeholder="e.g. space adventure, dark thriller, feel-good comedy")
top_n = st.slider("Number of recommendations", 1, 10, 5)

# Handle history chip click — runs at script level, not in callback
if st.session_state.history_click:
    q = st.session_state.history_click
    st.session_state.history_click = None
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
    ncols = 2
    for i in range(0, len(st.session_state.last_results), ncols):
        cols = st.columns(ncols)
        for j, rec in enumerate(st.session_state.last_results[i:i+ncols]):
            with cols[j]:
                with st.container(border=True):
                    st.markdown(f"##### {rec['title']}")
                    st.markdown(f"*{rec['genre']}* — Match: **{rec['score']*100:.1f}%**")
                    if rec.get('keywords'):
                        st.caption(f"Matched on: {', '.join(rec['keywords'])}")
                    key = f"mlt_{i}_{j}_{rec['title']}"
                    if st.button("More like this", key=key):
                        st.session_state.similar_source = rec["title"]
                        st.session_state.similar_results = recommender.recommend_similar(rec["title"], top_n=5)
                        st.rerun()

if st.session_state.similar_results:
    st.markdown("---")
    st.subheader(f"More like \"{st.session_state.similar_source}\"")
    ncols = 2
    for i in range(0, len(st.session_state.similar_results), ncols):
        cols = st.columns(ncols)
        for j, sr in enumerate(st.session_state.similar_results[i:i+ncols]):
            with cols[j]:
                with st.container(border=True):
                    st.markdown(f"##### {sr['title']}")
                    st.markdown(f"*{sr['genre']}* — Match: **{sr['score']*100:.1f}%**")
                    if sr.get('keywords'):
                        st.caption(f"Matched on: {', '.join(sr['keywords'])}")
