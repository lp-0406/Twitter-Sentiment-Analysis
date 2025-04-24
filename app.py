import streamlit as st
import pickle
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
import nltk
from twitter_client import fetch_user_tweets  # Now fetches from CSV

# Download stopwords once
def load_stopwords():
    nltk.download('stopwords')
    return stopwords.words('english')

# Load model and vectorizer once
@st.cache_resource
def load_resources():
    stop_words = load_stopwords()
    with open('model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
    with open('vectorizer.pkl', 'rb') as vectorizer_file:
        vectorizer = pickle.load(vectorizer_file)
    return stop_words, model, vectorizer

# Sentiment prediction
def predict_sentiment(text, model, vectorizer, stop_words):
    text = re.sub('[^a-zA-Z]', ' ', text)
    text = text.lower().split()
    text = [word for word in text if word not in stop_words]
    text = ' '.join(text)
    vect_text = vectorizer.transform([text])
    label = model.predict(vect_text)[0]
    return "Negative" if label == 0 else "Positive"

# Colored tweet card
def display_card(tweet_text, sentiment):
    color = "#2ecc71" if sentiment == "Positive" else "#e74c3c"
    st.markdown(
        f"""
        <div style="background-color: {color}; padding: 12px; border-radius: 8px; margin: 8px 0;">
            <strong style="color: white;">{sentiment} Sentiment</strong><br>
            <span style="color: white;">{tweet_text}</span>
        </div>
        """,
        unsafe_allow_html=True
    )

# Main App
def main():
    st.title("Twitter Sentiment Analysis")

    # Load model/vectorizer/stopwords
    stop_words, model, vectorizer = load_resources()

    # User selects mode
    option = st.selectbox("Choose an option:", ["Input Text", "Use Sample Tweets"])

    if option == "Input Text":
        text_input = st.text_area("Enter text to analyze sentiment:")
        if st.button("Analyze"):
            if text_input.strip():
                sentiment = predict_sentiment(text_input, model, vectorizer, stop_words)
                st.write(f"**Sentiment:** {sentiment}")
            else:
                st.warning("Please enter some text.")
    else:
        if st.button("Load Sample Tweets"):
            try:
                tweets = fetch_user_tweets(max_tweets=10)  # you can change this
                for tweet in tweets:
                    sentiment = predict_sentiment(tweet['text'], model, vectorizer, stop_words)
                    display_card(tweet['text'], sentiment)
            except Exception as e:
                st.error(f"Error loading sample tweets: {e}")

if __name__ == "__main__":
    main()
