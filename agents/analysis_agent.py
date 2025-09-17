class AnalysisAgent:
    def __init__(self):
        pass

    def harmonize(self, data_dict, sentiment_dict):
        insights = []
        for ticker in data_dict:
            sentiment = sentiment_dict.get(ticker, "N/A")
            insights.append(f"{ticker}: data points={len(data_dict[ticker])}, sentiment={sentiment}")
        return insights

# Test
if __name__ == "__main__":
    data = {"AAPL": [1,2,3], "BTC": [1,2,3,4]}
    sentiment = {"AAPL": "positive", "BTC": "neutral"}
    agent = AnalysisAgent()
    print(agent.harmonize(data, sentiment))
