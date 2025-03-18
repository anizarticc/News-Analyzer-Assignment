# News Summarization and Text-to-Speech Application

This is a web-based application that extracts key details from multiple news articles related to a given company, performs sentiment analysis, and generates a text-to-speech (TTS) output in Hindi.

## Features
- **News Extraction**: Fetches news articles related to a company.
- **Sentiment Analysis**: Analyzes the sentiment of each article (positive, negative, neutral).
- **Text-to-Speech**: Converts the summarized content into Hindi speech.
- **Gradio Interface**: Provides a simple web interface for user interaction.

---

## Setup Instructions

### Install Dependencies
pip install -r requirements.txt

### Run the Backend (FastAPI)
python api.py

### Run the Frontend (Gradio)
python app_gradio.py

### Access the Application
~ Open your browser and go to http://127.0.0.1:7860.
~ Enter a company name (e.g., "Tesla") and click Analyze News.
~ View the analysis and listen to the Hindi TTS output.

### Clone the Repository
```bash
git clone https://github.com/anizarticc/News-Summarization-and-Text-to-Speech-Application.git
cd News-Summarization-and-Text-to-Speech-Application
