from newsapi import NewsApiClient

class SentimentAgent:
    def __init__(self, api_key):
        self.newsapi = NewsApiClient(api_key=api_key)

    def fetch_headlines(self, tickers):
        headlines = []
        for ticker in tickers:
            all_articles = self.newsapi.get_everything(q=ticker, language='en', page_size=5)
            for article in all_articles['articles']:
                headlines.append(article['title'])
        return headlines

    def analyze(self, headlines):
        # Temporary placeholder: all neutral
        return {headline: "neutral" for headline in headlines}

# Test block
if __name__ == "__main__":
    agent = SentimentAgent("YOUR_NEWSAPI_KEY")
    headlines = agent.fetch_headlines(["AAPL", "BTC"])
    print(agent.analyze(headlines))
