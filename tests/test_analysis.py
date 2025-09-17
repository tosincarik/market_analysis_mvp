from agents.analysis_agent import AnalysisAgent

def test_harmonize_returns_list():
    agent = AnalysisAgent()
    data = {"AAPL": "data"}
    sentiment = {"AAPL": "positive"}
    insights = agent.harmonize(data, sentiment)
    assert isinstance(insights, list)
    assert "AAPL" in insights[0]
