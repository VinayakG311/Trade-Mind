from langchain_core.prompts import PromptTemplate



trade_prompt = PromptTemplate(
    input_variables=["symbol"],
    template="""
You are an AI trading assistant. For the given stock symbol "{symbol}":
1. Retrieve SMA(14), EMA(20), and RSI(14).
2. Based on these, decide: BUY / SELL / HOLD.
3. Provide a concise rationale referencing the indicators. IF any tools return any error then return that
```
Recommendation: BUY / SELL / HOLD
Rationale: <1-2 sentences>
Indicators:
  SMA14: <>
  EMA20: <>
  RSI14: <>
```
"""
)

# --- Compact (Small) Trade Prompt ---
trade_prompt_small = PromptTemplate(
    input_variables=["symbol", "timeframe"],
    template="""
Using Market Data and Indicator Engine, for {symbol} on {timeframe}:
• Fetch latest OHLC.
• Compute SMA(14), EMA(20), RSI(14).
• Recommend BUY/SELL/HOLD with a one-line rationale based on price vs moving averages and momentum.

Format:
Recommendation: <BUY/SELL/HOLD>
Rationale: <brief>
"""
)

# --- Moderate (Mid) Trade Prompt ---
trade_prompt_mid = PromptTemplate(
    input_variables=["symbol", "timeframe"],
    template="""
You are an AI trading assistant using:
- Market Data (OHLC + volume)
- Indicator Engine (SMA, EMA, RSI, MACD, BB)
- Volume Analysis (OBV, VWAP)

For {symbol} on {timeframe}:
1. Fetch OHLC and Volume (Market Data).
2. Compute indicators (Indicator Engine) and volume context (Volume Analysis).
3. Summarize:
   • Price vs SMA/EMA crossover.
   • Momentum: RSI and MACD signal.
   • Volatility: Bollinger Band width.
   • Volume trend: OBV direction, VWAP bias.
4. Recommend BUY/SELL/HOLD.
5. Provide 2–3 sentence rationale citing key indicator insights.

Output:
```
Recommendation: <BUY/SELL/HOLD>
Rationale: ...
```"""
)

# --- Detailed (Large) Trade Prompt ---
trade_prompt_large = PromptTemplate(
    input_variables=["symbol", "timeframe"],
    template="""
As an AI trading assistant with access to Market Data, Indicator Engine, and Volume Analysis:

Task for {symbol} on {timeframe}:
1. Fetch OHLC and volume.
2. Compute:
   - SMA(14), EMA(20)
   - RSI(14), MACD(12,26,9)
   - Bollinger Bands(20,2)
   - OBV, VWAP
3. Analyze:
   - Price relation to SMA/EMA (trend).
   - RSI for overbought/oversold.
   - MACD crossover direction.
   - Band width for volatility.
   - OBV and VWAP for volume confirmation.
4. Decide: BUY / SELL / HOLD.
5. Present methodology and values:
```
Recommendation: BUY / SELL / HOLD
Rationale: <1-2 sentences>
Indicators:
  Price: <>
  SMA14/EMA20: <>/<>
  RSI14: <>
  MACD: <macd> (signal <signal>)
  BB Lower/Mid/Upper: <>/<>/<>
  OBV: <>
  VWAP: <>
```"""
)

