from typing import TypedDict, Optional, Dict, Any
import pandas as pd

class StockAgentState(TypedDict):
    ticker: str
    historical_data: Optional[pd.DataFrame]
    current_price: Optional[float]
    sma_10: Optional[float]
    sma_20: Optional[float]
    rsi_14: Optional[float]
    recommendation: Optional[str]
    report: Optional[str]
    error: Optional[str]
