from graph import stock_agent_app

def main():
    ticker = input("Enter a stock ticker (e.g. AAPL): ").strip()
    if not ticker:
        ticker = "AAPL"
    
    initial_state = {
        "ticker": ticker,
        "historical_data": None,
        "current_price": None,
        "sma_10": None,
        "sma_20": None,
        "rsi_14": None,
        "recommendation": None,
        "report": None,
        "error": None
    }
    
    result = stock_agent_app.invoke(initial_state)
    print("\n" + "=" * 60)
    print(result.get("report", "Error generating report."))
    print("=" * 60)

if __name__ == "__main__":
    main()
