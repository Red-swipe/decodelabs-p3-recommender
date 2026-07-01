import streamlit as st

from engine.vectorizer import TextVectorizer
from engine.recommender import Recommender


@st.cache_resource
def load_engine():
    v = TextVectorizer()
    v.fit()
    return Recommender(v)


st.set_page_config(page_title="Movie Recommendation Engine", layout="centered")

st.title("Movie Recommendation Engine")
st.markdown("Content-Based Filtering using TF-IDF Similarity")

query = st.text_input(
    "Describe what you're in the mood for "
    "(e.g. space adventure, dark thriller, feel-good comedy)"
)

top_n = st.slider("Number of recommendations", min_value=1, max_value=10, value=5)

if st.button("Get Recommendations"):
    if not query or not query.strip():
        st.warning("Please describe what you want to watch.")
    else:
        recommender = load_engine()
        results = recommender.recommend(query.strip(), top_n=top_n)

        for rec in results:
            with st.container(border=True):
                st.markdown(f"### {rec['title']}")
                st.markdown(f"**{rec['genre']}**")
