import gradio as gr
import requests

# Function to analyze news
def analyze_news(company_name):
    try:
        # Call the backend API
        response = requests.post(
            "http://localhost:8000/analyze-news/",
            json={"company_name": company_name}
        )
        
        if response.status_code == 200:
            result = response.json()
            
            # Print the response for debugging
            print("Frontend Received:", result)
            
            # Prepare the analysis text
            analysis_text = f"### Company: {result['company']}\n\n"
            
            for article in result["articles"]:
                analysis_text += f"#### Title: {article['title']}\n"
                analysis_text += f"**Summary:** {article['summary']}\n"
                analysis_text += f"**Sentiment:** {article['sentiment']}\n"  # Ensure this key exists
                analysis_text += f"**Topics:** {', '.join(article['topics'])}\n"
                analysis_text += "---\n"
            
            analysis_text += "### Comparative Sentiment Analysis\n"
            analysis_text += str(result["sentiment_analysis"]) + "\n"
            
            # Get the TTS audio file path
            tts_output = result["tts_output"]
            
            # Return the analysis text first, then the audio file
            return analysis_text, tts_output
        else:
            return "Failed to fetch news. Please try again.", None
    except Exception as e:
        return f"An error occurred: {e}", None

# Gradio interface
iface = gr.Interface(
    fn=analyze_news,  # Function to call
    inputs=gr.Textbox(label="Enter the company name"),  # Input field
    outputs=[
        gr.Markdown(label="Analysis Result"),  # Output for text analysis
        gr.Audio(label="Hindi Text-to-Speech Output")  # Output for audio
    ],
    title="News Summarization and Sentiment Analysis",
    description="Enter a company name to analyze news articles and generate a sentiment report with Hindi TTS."
)

# Launch the Gradio app
iface.launch()