import requests
from bs4 import BeautifulSoup
from transformers import pipeline  # Import pipeline from transformers
from gtts import gTTS  # Import gTTS from gtts
import os

# Mock data for testing
MOCK_ARTICLES = [
    {
        "title": "Tesla's New Model Breaks Sales Records",
        "summary": "Tesla's latest model sees record sales in Q3...",
        "content": "Tesla's latest model has seen record sales in Q3, driven by strong demand for electric vehicles.",
        "topics": ["Electric Vehicles", "Stock Market", "Innovation"]
    },
    {
        "title": "Regulatory Scrutiny on Tesla's Self-Driving Tech",
        "summary": "Regulators have raised concerns over Tesla's self-driving software...",
        "content": "Regulators have raised concerns over Tesla's self-driving software, citing safety issues.",
        "topics": ["Regulations", "Autonomous Vehicles"]
    }
]

def fetch_news(company_name):
    # For now, return mock data
    return MOCK_ARTICLES

def summarize_articles(articles):
    # Initialize the summarization pipeline
    summarizer = pipeline("summarization")
    summarized_articles = []
    
    for article in articles:
        # Summarize the article content
        summary = summarizer(article["content"], max_length=50, min_length=25, do_sample=False)
        summarized_articles.append({
            "title": article["title"],
            "summary": summary[0]["summary_text"],
            "topics": article["topics"]
        })
    
    return summarized_articles

def analyze_sentiment(articles):
    # Initialize the sentiment analysis pipeline
    sentiment_pipeline = pipeline("sentiment-analysis")
    sentiment_results = []
    
    for article in articles:
        # Analyze the sentiment of the article summary
        sentiment = sentiment_pipeline(article["summary"])[0]
        article["sentiment"] = sentiment["label"]  # Add sentiment to the article
        sentiment_results.append({
            "title": article["title"],
            "sentiment": sentiment["label"],
            "score": sentiment["score"]
        })
    
    return sentiment_results

def generate_tts(sentiment_results):
    # Generate text for TTS
    text = " ".join([f"{result['title']} has a {result['sentiment']} sentiment." for result in sentiment_results])
    
    # Convert text to Hindi speech
    tts = gTTS(text=text, lang='hi')
    tts.save("output.mp3")
    
    print("TTS file saved at:", os.path.abspath("output.mp3"))  # Print absolute path
    return "output.mp3"
import os

def generate_tts(sentiment_results):
    # Generate text for TTS
    text = " ".join([f"{result['title']} has a {result['sentiment']} sentiment." for result in sentiment_results])
    
    # Convert text to Hindi speech
    tts = gTTS(text=text, lang='hi')
    file_path = os.path.abspath("output.mp3")  # Use absolute path
    tts.save(file_path)
    
    print("TTS file saved at:", file_path)  # Print absolute path
    return file_path