

---

````markdown
# Sentiment Analysis Web Application

This project is a full-stack sentiment analysis web application that uses machine learning to classify text as **Positive** or **Negative**. It is built with a **Flask-based REST API** on the backend and a **Streamlit interface** on the frontend. The model is trained on the **Amazon Alexa Reviews dataset**, a publicly available dataset released by Amazon.

---

## 💡 Overview

- Predict sentiment from individual sentences.
- Perform batch sentiment analysis by uploading a CSV file.
- Visualize sentiment distribution with a pie chart.
- Download predictions as a CSV file.

---

## 🚀 Technologies Used

- **Python 3**
- **Flask** — RESTful API backend
- **Streamlit** — Interactive frontend interface
- **Scikit-learn** & **XGBoost** — Machine learning model
- **NLTK** — Text preprocessing and stemming
- **Pandas, Matplotlib** — Data manipulation and visualization

---

## 📊 Dataset

The model is trained on the [Amazon Alexa Reviews dataset](https://www.kaggle.com/sid321axn/amazon-alexa-reviews), which contains thousands of customer reviews labeled as positive or negative.

---

## 🛠️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/<your-repo>](https://github.com/c0mradebat/Sentiment-Analysis.git
cd Sentiment-Analysis
````

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> Make sure to run:
>
> ```python
> import nltk
> nltk.download('stopwords')
> ```

---

## 📦 Running the Application

### Step 1: Start Flask API

```bash
python api.py
```

### Step 2: Start Streamlit Frontend (in a new terminal)

```bash
streamlit run main.py
```

Navigate to the URL shown in your terminal (usually `http://localhost:8501`).

---

## 🖼️ Features

* **Single Sentence Prediction**
  Input a sentence and instantly get the predicted sentiment.

* **Bulk Prediction via CSV Upload**
  Upload a CSV with a column named `Sentence` and receive predicted sentiments for each row.

* **Graphical Insights**
  Automatically generated pie chart showing sentiment distribution.

* **CSV Download**
  Download the results with predictions directly from the app.

---

## 📄 Example Input Format (CSV)

| Sentence                   |
| -------------------------- |
| I love this product!       |
| Alexa does not understand. |
| Worst experience ever.     |

---

## 📬 Contact

For questions or suggestions, feel free to reach out via [GitHub Issues]

---

© 2025 — Built with ❤️ 


