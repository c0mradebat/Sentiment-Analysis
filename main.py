import streamlit as st
import pandas as pd
import requests
from io import BytesIO

# Update this if your Flask API runs on a different port
prediction_endpoint = "http://127.0.0.1:5000/predict"

st.title("Text Sentiment Predictor")

uploaded_file = st.file_uploader(
    "Choose a CSV file for bulk prediction - Upload the file and click on Predict",
    type="csv",
)

# Text input for sentiment prediction
user_input = st.text_input("Enter text and click on Predict", "")

# Prediction logic
if st.button("Predict"):
    if uploaded_file is not None:
        try:
            # Send file for prediction
            files = {"file": uploaded_file.getvalue()}
            response = requests.post(prediction_endpoint, files=files)

            # Handle errors
            if response.status_code != 200:
                st.error("Error from API: " + response.text)
            else:
                # Convert to DataFrame
                response_bytes = BytesIO(response.content)
                result_df = pd.read_csv(response_bytes)

                st.write("Predictions:")
                st.dataframe(result_df)

                st.download_button(
                    label="Download Predictions",
                    data=response.content,
                    file_name="Predictions.csv",
                    mime="text/csv",
                )
        except Exception as e:
            st.error(f"Something went wrong: {e}")
    elif user_input.strip() != "":
        try:
            # Send JSON text for prediction
            response = requests.post(prediction_endpoint, json={"text": user_input})

            if response.status_code != 200:
                st.error("Error from API: " + response.text)
            else:
                result = response.json()
                st.write(f"Predicted sentiment: **{result['prediction']}**")

        except Exception as e:
            st.error(f"Failed to get prediction: {e}")
            st.text(response.text)
    else:
        st.warning("Please upload a CSV file or enter text for prediction.")
