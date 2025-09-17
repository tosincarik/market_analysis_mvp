from agents.data_retrieval_agent import DataRetrievalAgent

def test_fetch_returns_dict():
    agent = DataRetrievalAgent(["AAPL", "BTC"])
    data = agent.fetch()
    assert isinstance(data, dict)
    assert "AAPL" in data and "BTC" in data
