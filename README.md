# V2 — Enhanced Recommender

> **DecodeLabs AI Internship — Project 3 — V2**  
> Content-based movie recommender with genre filter, score percentages, card grid, and search history.

---

## What's New Over V1

- ✅ Genre filter sidebar to narrow results
- ✅ Similarity scores displayed as percentages
- ✅ "More like this" button per result — find similar movies from any result
- ✅ Card grid layout with poster placeholders
- ✅ Session-based search history (text display)

## What It Still Lacks vs V3

- ❌ No hybrid scoring formula (pure TF-IDF only)
- ❌ No keyword explainability ("Matched on: ...")
- ❌ No clickable search history chips
- ❌ No dark theme

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
├── app.py                 # Streamlit UI (V2)
├── engine/
│   ├── recommender.py     # Cosine similarity logic
│   ├── vectorizer.py      # TF-IDF vectorization
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
