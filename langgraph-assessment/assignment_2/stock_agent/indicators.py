import pandas as pd

def compute_sma(hist: pd.DataFrame, window: int) -> float:
    return float(hist['Close'].rolling(window=window).mean().iloc[-1])

def compute_rsi(hist: pd.DataFrame, window: int = 14) -> float:
    delta = hist['Close'].diff()
    gain = delta.clip(lower=0)
    loss = -1 * delta.clip(upper=0)
    
    ema_gain = gain.ewm(com=window-1, adjust=False).mean()
    ema_loss = loss.ewm(com=window-1, adjust=False).mean()
    
    rs = ema_gain / ema_loss
    rsi_14 = 100 - (100 / (1 + rs))
    return float(rsi_14.iloc[-1])
