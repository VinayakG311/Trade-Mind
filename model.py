from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.agents import Tool, initialize_agent, AgentType
import os
from dotenv import load_dotenv
from tools import *
from prompts_trade import *
load_dotenv()

ALPHA_VANTAGE_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_BASE = os.getenv("OPENROUTER_BASE")
tools = [
    Tool(
        name="Technical Analysis",
        func=get_technical_snapshot,
        description="Provides comprehensive technical indicators including SMA, RSI, MACD, and Bollinger Bands"
    ),
    Tool(
        name="Volume Analysis",
        func=get_volume_analysis,
        description="Provides comprehensive volume metrics including OBV, VWAP, volume spikes, and trend analysis"
    ),
    Tool(
        name="Volatility Metrics",
        func=get_volatility_metrics,
        description="Provides comprehensive volatility metrics using bollinger width , ATR etc"
    ),

]


llm = ChatOpenAI(
    model_name="deepseek/deepseek-chat-v3-0324:free",
    openai_api_key=OPENROUTER_API_KEY,
    openai_api_base=OPENROUTER_BASE,
)
trade_agent = initialize_agent(
    tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=False,handle_parsing_errors=True
)

trade_agent.run("""
You are an AI trading assistant. For the given stock symbol "AAPL":
1. Retrieve SMA(14), EMA(20), and RSI(14).
2. Based on these, decide: BUY / SELL / HOLD.
3. Provide a concise rationale referencing the indicators. IF any tools return any error then return that
```
Recommendation: BUY / SELL / HOLD and for how much duration.
Rationale: <1-2 sentences>
Indicators:
  SMA14: <>
  EMA20: <>
  RSI14: <>
```
""")