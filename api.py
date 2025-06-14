from flask import Flask, request, jsonify, send_file, render_template
import re
from io import BytesIO
import matplotlib.pyplot as plt
import pandas as pd
import base64

import nltk
nltk.download("stopwords")
nltk.download("vader_lexicon")

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.sentiment.vader import SentimentIntensityAnalyzer

STOPWORDS = set(stopwords.words("english"))
stemmer = PorterStemmer()
sid = SentimentIntensityAnalyzer()

app = Flask(__name__)


@app.route("/test", methods=["GET"])
def test():
    return jsonify({"message": "Test request received successfully. Service is running."})


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("landing.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        if "file" in request.files:
            file = request.files["file"]
            data = pd.read_csv(file)
            predictions, graph = bulk_prediction(data)

            response = send_file(
                predictions,
                mimetype="text/csv",
                as_attachment=True,
                download_name="Predictions.csv",
            )

            response.headers["X-Graph-Exists"] = "true"
            response.headers["X-Graph-Data"] = base64.b64encode(graph.getbuffer()).decode("ascii")

            return jsonify({"message": "File processed successfully", "graph_exists": True})

        elif "text" in request.json:
            text_input = request.json["text"]
            predicted_sentiment = single_prediction(text_input)
            return jsonify({"message": "Prediction successful", "prediction": predicted_sentiment})

    except Exception as e:
        return jsonify({"error": str(e)})


def single_prediction(text_input):
    score = sid.polarity_scores(text_input)["compound"]
    return "Positive" if score >= 0 else "Negative"


def bulk_prediction(data):
    sentiments = []
    for sentence in data["Sentence"]:
        score = sid.polarity_scores(sentence)["compound"]
        sentiments.append("Positive" if score >= 0 else "Negative")

    data["Predicted sentiment"] = sentiments
    predictions_csv = BytesIO()
    data.to_csv(predictions_csv, index=False)
    predictions_csv.seek(0)

    graph = get_distribution_graph(data)

    return predictions_csv, graph


def get_distribution_graph(data):
    fig = plt.figure(figsize=(5, 5))
    colors = ("green", "red")
    wp = {"linewidth": 1, "edgecolor": "black"}
    tags = data["Predicted sentiment"].value_counts()
    explode = (0.01, 0.01)

    tags.plot(
        kind="pie",
        autopct="%1.1f%%",
        shadow=True,
        colors=colors,
        startangle=90,
        wedgeprops=wp,
        explode=explode,
        title="Sentiment Distribution",
        xlabel="",
        ylabel="",
    )

    graph = BytesIO()
    plt.savefig(graph, format="png")
    plt.close()

    return graph


if __name__ == "__main__":
    app.run(port=5000, debug=True)
