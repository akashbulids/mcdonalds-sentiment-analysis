import streamlit as st
import tensorflow as tf
import joblib
import re
import numpy as np

from tensorflow.keras.preprocessing.sequence import pad_sequences




model =joblib.load("model/LSTM_MODEL.pkl")
tokenizer = joblib.load("model/tokenizer.pkl")




def clean_text(text):

    text = text.lower()

    # Remove URL
    text = re.sub(
        r"http\S+|www\S+|https\S+",
        "",
        text
    )

    # Remove special characters
    text = re.sub(
        r"[^a-zA-Z\s]",
        "",
        text
    )

    # Remove extra spaces
    text = re.sub(
        r"\s+",
        " ",
        text
    ).strip()

    return text


# ==========================================
# PREDICTION FUNCTION
# ==========================================

def predict_sentiment(text):

    # Cleaning
    clean = clean_text(text)

    # Tokenization
    sequence = tokenizer.texts_to_sequences([clean])

    # Padding
    padded = pad_sequences(
        sequence,
        maxlen=300,
        padding="post",
        truncating="post"
    )

    # Prediction
    prediction = model.predict(
        padded,
        verbose=0
    )[0]

    return prediction


# ==========================================
# STREAMLIT UI
# ==========================================

st.title("😊 Sentiment Analysis App")

st.write(
    "Enter a review and predict the sentiment"
)


# Text input
user_input = st.text_area(
    "Enter text for sentiment analysis:"
)


# ==========================================
# PREDICT BUTTON
# ==========================================

if st.button("Predict Sentiment"):

    if user_input.strip():

        # Get prediction
        pred = predict_sentiment(user_input)

        # Get class
        predicted_class = np.argmax(pred)


        # ==================================
        # YOUR ACTUAL LABEL MAPPING
        # ==================================

        labels = {
            0: "Negative",
            1: "Positive",
            2: "Neutral"
        }

        sentiment = labels[predicted_class]


        # ==================================
        # DISPLAY RESULT
        # ==================================

        st.subheader(
            f"Sentiment: **{sentiment}**"
        )


     
        # DISPLAY SCORES
    

        st.write("### Prediction Scores")

        st.write(
            f"🔴 Negative: {pred[0]:.2%}"
        )

        st.write(
            f"🟢 Positive: {pred[1]:.2%}"
        )

        st.write(
            f"🟡 Neutral: {pred[2]:.2%}"
        )
    else:

        st.warning(
            "Please enter some text."
        )