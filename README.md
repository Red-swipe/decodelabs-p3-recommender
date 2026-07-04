# Movie Recommendation Engine

> **DecodeLabs AI Internship — Project 3, Version 3**  
> Content-based movie recommendation system using TF-IDF and cosine similarity with an interactive Streamlit UI.

---

## What It Does

Enter any movie genre, keyword, or interest — the engine finds the most similar movies from a real dataset using natural language similarity, not random guesses.

**Example:** Type `"sci-fi space exploration"` → get movies ranked by how closely they match that profile.

### Version History

| Version | Features |
|---------|----------|
| **V1** | Basic TF-IDF — single query, plain text results, 3 columns |
| **V2** | Genre filter, score %, card grid, "More like this", search history, IMDB placeholder |
| **V3** | Hybrid scoring (content 70% + genre 30%), matched keywords per result, dark theme, 2-column grid, clickable history chips |

---

## How It Works

| Layer | Technology |
|-------|-----------|
| **Vectorization** | TF-IDF (Term Frequency-Inverse Document Frequency) |
| **Similarity** | Cosine Similarity via scikit-learn |
| **UI** | Streamlit |
| **Data** | movies.csv (titles, genres, descriptions) |

**Pipeline:**
1. Movie metadata → TF-IDF matrix (built once at startup)
2. User query → TF-IDF vector
3. Cosine similarity computed between query vector and all movies
4. Optional genre filter applied
5. Top-N results returned ranked by score

---

## Getting Started

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

## Project Structure

```
decodelabs-p3-recommender/
├── app.py                 # Streamlit UI (V3)
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

## Skills Demonstrated

- Content-based filtering from scratch (no ML frameworks doing the heavy lifting)
- TF-IDF vectorization and cosine similarity
- Building a recommendation pipeline end-to-end
- Clean modular Python architecture (engine separation)
- Streamlit for rapid ML app deployment
- Interactive UI with filters, cards, and session state

---

## License

MIT — see [LICENSE](LICENSE)

---

*Built as part of the DecodeLabs AI Engineer Training Program, 2025.*
