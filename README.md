# 🎬 Movie Recommendation Engine

> **DecodeLabs AI Internship — Project 3**  
> Content-based movie recommendation system using TF-IDF, cosine similarity, and hybrid scoring.

---

## 🚀 Getting Started

```bash
# Clone the repo
git clone https://github.com/Red-swipe/decodelabs-p3-recommender.git
cd decodelabs-p3-recommender

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

Open `http://localhost:8501` in your browser.

---

## 📁 Project Structure

```
decodelabs-p3-recommender/
├── app.py                 # Streamlit UI
├── engine/
│   ├── recommender.py     # Cosine similarity + hybrid scoring logic
│   ├── vectorizer.py      # TF-IDF vectorization (content + genre)
│   └── __init__.py
├── data/
│   └── movies.csv         # Movie dataset
├── requirements.txt
├── LICENSE
└── README.md
```

---

## Version History

### V1 — Basic Recommender
- TF-IDF cosine similarity on movie metadata
- Simple list output of top-N results
- Minimal Streamlit UI

### V2 — Enhanced Experience
- Genre filter sidebar
- Similarity scores displayed as percentages
- "More like this" button per result
- Card grid layout
- Session-based search history (text display)

### V3 — Portfolio Quality
- Hybrid scoring: 0.7 × content similarity + 0.3 × genre match ratio
- Explainability: "Matched on: [top 3 keywords]" under each result
- Clickable search history chips in sidebar (last 5 queries, re-runnable)
- Dark theme UI
- 2-column card grid

---

## 📜 License

MIT — see [LICENSE](LICENSE)

---

*Built as part of the DecodeLabs AI Engineer Training Program, 2025.*