import talib
import yfinance as yf
import numpy as np
from typing import Dict, Union

from talib import MA_Type


def get_technical_snapshot(symbol: str, period: str = "200d") -> Dict[str, Union[float, dict]]:
    """
    Returns multiple technical indicators using TA-Lib
    """
    try:
        df = yf.download(symbol, period=period)
        if df.empty:
            return {"error": "No data found"}

        close = df['Close'].values
        high = df['High'].values
        low = df['Low'].values

        # SMA Calculations
        sma_values = {
            'SMA_14': talib.SMA(close, timeperiod=14)[-1],
            'SMA_50': talib.SMA(close, timeperiod=50)[-1],
            'SMA_200': talib.SMA(close, timeperiod=200)[-1]
        }

        # RSI Calculation
        rsi = talib.RSI(close, timeperiod=14)[-1]

        # MACD Calculation
        macd, signal, hist = talib.MACD(close, fastperiod=12, slowperiod=26, signalperiod=9)
        macd_values = {
            'MACD': macd[-1],
            'Signal': signal[-1],
            'Histogram': hist[-1]
        }

        # Bollinger Bands Calculation
        upper, middle, lower = talib.BBANDS(close, timeperiod=20, nbdevup=2, nbdevdn=2, matype=MA_Type.SMA)
        bollinger_values = {
            'Upper': upper[-1],
            'Middle': middle[-1],
            'Lower': lower[-1]
        }

        return {
            'SMA': sma_values,
            'RSI': round(rsi, 2),
            'MACD': {k: round(v, 4) for k, v in macd_values.items()},
            'Bollinger': {k: round(v, 4) for k, v in bollinger_values.items()}
        }

    except Exception as e:
        return {"error": str(e)}

def get_volume_analysis(symbol: str, period: str = "3mo") -> Dict[str, Union[float, dict]]:
    """
    Computes volume analysis using TA-Lib
    """
    try:
        df = yf.download(symbol, period=period)
        if df.empty:
            return {"error": "No data found"}

        close = df['Close'].values
        high = df['High'].values
        low = df['Low'].values
        volume = df['Volume'].values.astype(float)

        # Volume indicators
        obv = talib.OBV(close, volume)
        volume_sma = talib.SMA(volume, timeperiod=20)

        # Manual VWAP calculation
        typical_price = (high + low + close) / 3
        cumulative_vp = np.cumsum(typical_price * volume)
        cumulative_vol = np.cumsum(volume)
        vwap = cumulative_vp / cumulative_vol

        # Volume patterns
        latest_volume = volume[-1]
        avg_volume = np.mean(volume)
        volume_spike = latest_volume > 2 * avg_volume
        volume_trend = "Up" if latest_volume > volume[-5] else "Down"

        # Accumulation/Distribution Line
        ad = talib.AD(high, low, close, volume)

        return {
            'volume_metrics': {
                'latest': int(latest_volume),
                '20d_avg': int(avg_volume),
                'obv': round(obv[-1], 2),
                'vwap': round(vwap[-1], 2),
                'sma_20': int(volume_sma[-1]) if not np.isnan(volume_sma[-1]) else None
            },
            'volume_patterns': {
                'spike': volume_spike,
                'trend': volume_trend,
                'recent_ratio': round(latest_volume / avg_volume, 2)
            },
            'volume_oscillators': {
                'volume_roc': round(((latest_volume / volume[-5]) - 1) * 100, 2),
                'volume_ad': round(ad[-1], 2)
            }
        }

    except Exception as e:
        return {"error": str(e)}

def get_volatility_metrics(symbol: str, period: str = "1y") -> Dict[str, float]:
    """
    Calculates volatility metrics using TA-Lib
    """
    try:
        df = yf.download(symbol, period=period)
        if df.empty:
            return {"error": "No data found"}

        close = df['Close'].values
        high = df['High'].values
        low = df['Low'].values

        # ATR Calculation
        atr = talib.ATR(high, low, close, timeperiod=14)[-1]

        # Bollinger Band Width Calculation
        upper, middle, lower = talib.BBANDS(close, timeperiod=20, nbdevup=2, nbdevdn=2, matype=MA_Type.SMA)
        bb_width = (upper[-1] - lower[-1]) / middle[-1]

        # Historical Volatility
        returns = np.log(close[1:]/close[:-1])
        hist_vol = np.std(returns[-30:]) * np.sqrt(252)

        return {
            'ATR_14': round(atr, 2),
            'Bollinger_Width': round(bb_width, 4),
            '30D_Volatility': round(hist_vol, 4)
        }

    except Exception as e:
        return {"error": str(e)}