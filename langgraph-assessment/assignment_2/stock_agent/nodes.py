import yfinance as yf
from .state import StockAgentState
from .indicators import compute_sma, compute_rsi

def fetch_data(state: StockAgentState) -> StockAgentState:
    ticker = state["ticker"]
    try:
        stock = yf.Ticker(ticker)
        hist = stock.history(period="60d")
        if hist.empty:
            return {"error": f"No data found for ticker '{ticker}'."}
        current_price = hist['Close'].iloc[-1]
        return {"historical_data": hist, "current_price": current_price}
    except Exception as e:
        return {"error": f"Failed to fetch data for '{ticker}': {str(e)}"}

def calculate_indicators(state: StockAgentState) -> StockAgentState:
    if state.get("error"):
        return state
    hist = state["historical_data"]
    sma_10 = compute_sma(hist, 10)
    sma_20 = compute_sma(hist, 20)
    rsi_14 = compute_rsi(hist, 14)
    return {
        "sma_10": sma_10, 
        "sma_20": sma_20, 
        "rsi_14": rsi_14
    }

def generate_recommendation(state: StockAgentState) -> StockAgentState:
    if state.get("error"):
        return state
    sma_10 = state["sma_10"]
    sma_20 = state["sma_20"]
    rsi = state["rsi_14"]
    recommendation = "HOLD"
    if sma_10 > sma_20 and rsi < 70:
        recommendation = "BUY"
    elif sma_10 < sma_20 and rsi > 30:
        recommendation = "SELL"
    return {"recommendation": recommendation}

def format_report(state: StockAgentState) -> StockAgentState:
    if state.get("error"):
        report = f"### Stock Analysis Report: {state['ticker']}\n\n**Error:** {state['error']}"
        return {"report": report}
    report = f"""### Stock Analysis Report: {state['ticker']}

**Current Price:** ${state['current_price']:.2f}

**Technical Indicators:**
- 10-Day SMA: ${state['sma_10']:.2f}
- 20-Day SMA: ${state['sma_20']:.2f}
- 14-Day RSI: {state['rsi_14']:.2f}

**Recommendation:** **{state['recommendation']}**
"""
    return {"report": report}
