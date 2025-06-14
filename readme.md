Here’s a complete `README.md` file for your sentiment analysis project with Flask + Streamlit:

---

```markdown
# Sentiment Analysis Web App

This project is a **sentiment analysis** application built using **Flask** for the backend (API) and **Streamlit** for the frontend interface. It supports **single-text prediction** as well as **bulk prediction from CSV files**. The model classifies text into **Positive** or **Negative** sentiments.

---

## 📁 Folder Structure

```

├── api.py                  # Flask backend
├── main.py                 # Streamlit frontend
├── Models/                 # Contains ML model, scaler, and vectorizer
│   ├── model\_xgb.pkl
│   ├── scaler.pkl
│   └── countVectorizer.pkl
├── templates/
│   └── landing.html        # Flask landing page
├── .gitignore              # Git ignore file (excludes datasets)
├── README.md               # Project documentation
└── dataset/                # Ignored folder with raw data (not pushed to GitHub)

````

---

## 🔧 Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
````

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate        # On Linux/macOS
venv\Scripts\activate           # On Windows
```

### 3. Install requirements

```bash
pip install -r requirements.txt
```

If `requirements.txt` doesn't exist, install manually:

```bash
pip install flask streamlit pandas scikit-learn matplotlib nltk xgboost
```

Also download NLTK stopwords:

```python
import nltk
nltk.download('stopwords')
```

---

## 🚀 Run the App

### 1. Start the Flask API server

```bash
python api.py
```

### 2. In a separate terminal, run the Streamlit app

```bash
streamlit run main.py
```

Open the link shown in the terminal (usually `http://localhost:8501`).

---

## 📌 Features

* 🔍 Predict sentiment for a **single sentence**
* 📂 Upload CSV with a `Sentence` column to get **bulk predictions**
* 📊 Pie chart for sentiment distribution
* 💾 Download predictions as a `.csv` file

---
