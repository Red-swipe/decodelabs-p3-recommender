# V1 — Basic TF-IDF Movie Recommender

> **DecodeLabs AI Internship — Project 3 — V1**  
> Pure TF-IDF cosine similarity recommender with a minimal Streamlit UI.

---

## What It Does

Enter a movie genre or keyword — the engine returns top-N matching movies using TF-IDF cosine similarity on metadata. No genre weighting, no similarity scores shown. Simple list output.

## What It Does NOT Have

- ❌ No genre filter sidebar
- ❌ No similarity scores displayed
- ❌ No "More like this" buttons
- ❌ No card grid layout
- ❌ No explainability (matched keywords)
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
├── app.py                 # Streamlit UI
├── engine/
│   ├── recommender.py     # Cosine similarity
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