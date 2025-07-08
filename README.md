# Twitter-Sentiment-Analysis

A machine learning-powered web app that analyzes the **sentiment of tweets** and classifies them as **Positive** or **Negative**. Built using **Streamlit** and trained on real Twitter data.

---

## 🚀 Deployed App

Access the live app here:  
👉 [Twitter Sentiment Analysis - Streamlit](https://your-deployed-link.streamlit.app)

---

## Demo

![image](https://github.com/user-attachments/assets/73c71c24-2240-4388-af2c-893f43317091)

---

## Features

- Analyze sentiments of tweets in real-time
- Upload your own CSV of tweets or input manually
- Interactive interface with sentiment results
- Uses machine learning for prediction
- Visualizations for output interpretation

---

## Tech Stack

- **Python**
- **Streamlit** – frontend framework
- **Scikit-learn** – model building and evaluation
- **Pandas**, **NumPy** – data processing
- **Pickle** – model & vectorizer serialization
- **Matplotlib**, **Seaborn** – visualization (if used)

---

## Model Details

- **Algorithm Used:** Logistic Regression
- **Vectorization Method:** TF-IDF (Term Frequency–Inverse Document Frequency)
- **Dataset:** Labeled tweets from `sample_tweets.csv`
- **Classes:** Positive, Negative
- **Train-Test Split:** 80% Training / 20% Testing

---

## 📈 Model Performance

| Metric     | Score    |
|------------|----------|
| Accuracy   | **87.5%** |
| Precision  | 86.3%    |
| Recall     | 85.9%    |
| F1 Score   | 86.1%    |
