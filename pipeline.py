import os
from dotenv import load_dotenv
from agents.data_retrieval_agent import DataRetrievalAgent
from agents.sentiment_agent import SentimentAgent
from agents.analysis_agent import AnalysisAgent
from openai import OpenAI
from collections import Counter

# Load environment variables
load_dotenv()
news_api_key = os.getenv("YOUR_NEWSAPI_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=openai_api_key)

# Map tickers to keywords for headline matching
TICKER_KEYWORDS = {
    "AAPL": ["Apple"],
    "bitcoin": ["Bitcoin", "BTC"]
}

def gpt_sentiment_score(headlines):
    """Classify sentiment of headlines using GPT"""
    if not headlines:
        return {}
    import json

    prompt = (
        "Classify the sentiment of the following news headlines as positive, negative, or neutral.\n\n"
        f"Headlines:\n" + "\n".join(headlines) + "\n\n"
        "Return a JSON dictionary where keys are headlines and values are sentiment labels."
    )

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        content = response.choices[0].message.content
        sentiment_dict = json.loads(content)
    except Exception as e:
        print("GPT call failed, falling back to neutral sentiment:", e)
        sentiment_dict = {h: "neutral" for h in headlines}

    return sentiment_dict

def map_headlines_to_tickers(headlines, ticker_keywords):
    """Assign each headline to tickers based on keywords"""
    ticker_headlines = {ticker: [] for ticker in ticker_keywords}
    for hl in headlines:
        for ticker, keywords in ticker_keywords.items():
            if any(k.lower() in hl.lower() for k in keywords):
                ticker_headlines[ticker].append(hl)
    return ticker_headlines

def aggregate_sentiment(ticker_headlines, headline_sentiments):
    """Aggregate sentiment per ticker using majority vote"""
    ticker_sentiment = {}
    for ticker, hls in ticker_headlines.items():
        if not hls:
            ticker_sentiment[ticker] = "N/A"
            continue
        sentiments = [headline_sentiments.get(h, "neutral") for h in hls]
        most_common = Counter(sentiments).most_common(1)[0][0]
        ticker_sentiment[ticker] = most_common
    return ticker_sentiment

def run_pipeline(stocks, cryptos, news_api_key):
    # 1. Fetch data
    data_agent = DataRetrievalAgent(stocks=stocks, cryptos=cryptos)
    data = data_agent.fetch()  # fetch_stocks() + fetch_cryptos() internally
    tickers = list(data.keys())

    # 2. Fetch headlines
    sentiment_agent = SentimentAgent(news_api_key)
    headlines = sentiment_agent.fetch_headlines(tickers)
    print("Fetched headlines:", headlines)

    # 3. Get sentiment for each headline
    headline_sentiments = gpt_sentiment_score(headlines)

    # 4. Map headlines to tickers using keywords
    ticker_headlines = map_headlines_to_tickers(headlines, TICKER_KEYWORDS)

    # 5. Aggregate sentiment per ticker
    ticker_sentiment = aggregate_sentiment(ticker_headlines, headline_sentiments)

    # 6. Harmonize insights
    analysis_agent = AnalysisAgent()
    insights = analysis_agent.harmonize(data, ticker_sentiment)

    return insights

# Test
if __name__ == "__main__":
    stocks = ["AAPL"]
    cryptos = ["bitcoin"]
    results = run_pipeline(stocks, cryptos, news_api_key)
    print("Final Insights:", results)
