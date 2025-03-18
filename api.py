from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from utils import fetch_news, summarize_articles, analyze_sentiment, generate_tts

app = FastAPI()

class CompanyRequest(BaseModel):
    company_name: str

@app.post("/analyze-news/")
async def analyze_news(request: CompanyRequest):
    company_name = request.company_name

    try:
        # Fetch news articles
        articles = fetch_news(company_name)
        
        # Summarize articles
        summarized_articles = summarize_articles(articles)
        
        # Perform sentiment analysis
        sentiment_results = analyze_sentiment(summarized_articles)
        
        # Generate TTS in Hindi
        tts_output = generate_tts(sentiment_results)
        
        return {
            "company": company_name,
            "articles": summarized_articles,
            "sentiment_analysis": sentiment_results,
            "tts_output": tts_output
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)