from agents.sentiment_agent import SentimentAgent

def test_analyze_returns_dict():
    agent = SentimentAgent("fake_key")
    headlines = ["Stock up today", "Bitcoin falls"]
    sentiment = agent.analyze(headlines)
    assert isinstance(sentiment, dict)
    assert sentiment[headlines[0]] == "neutral"
