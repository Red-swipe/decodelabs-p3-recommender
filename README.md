# V3 — Hybrid Scoring + Explainability (Portfolio Quality)

> **DecodeLabs AI Internship — Project 3 — V3**  
> Content-based movie recommender with hybrid scoring, keyword explainability, clickable history chips, and dark theme UI.

---

## Full Feature List

- ✅ Hybrid scoring: 0.7 × content similarity (TF-IDF) + 0.3 × genre match ratio
- ✅ Explainability: "Matched on: [top 3 keywords]" under each result
- ✅ Clickable search history chips in sidebar (last 5 queries, re-runnable)
- ✅ Dark theme UI
- ✅ 2-column card grid with poster placeholders
- ✅ Genre filter sidebar
- ✅ Similarity scores displayed as percentages
- ✅ "More like this" button per result
- ✅ Session-based search history

## What's New Over V2

| V2 | V3 |
|---|---|
| Pure TF-IDF cosine similarity | Hybrid: 70% content + 30% genre |
| No explainability | "Matched on: [top 3 keywords]" per card |
| Text-only history display | Clickable history chips (re-runnable) |
| Light theme | Dark theme UI |

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
├── app.py                 # Streamlit UI (V3)
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

## 📜 License

MIT — see [LICENSE](LICENSE)

---

*Built as part of the DecodeLabs AI Engineer Training Program, 2025.*
