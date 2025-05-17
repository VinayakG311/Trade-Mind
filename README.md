# 🧠 Trade-Mind

**Trade-Mind** is an intelligent trading agent designed to assist users in making informed decisions in the stock market. Leveraging advanced machine learning techniques, it provides insightful analyses and predictions to empower users in their trading endeavors.

## 🚀 Features

* **Data Acquisition**: Fetches real-time and historical stock data for comprehensive analysis.
* **Data Preprocessing**: Cleans and prepares data to ensure optimal model performance.
* **Predictive Modeling**: Implements machine learning models to forecast stock price movements.
* **Performance Evaluation**: Assesses model accuracy using metrics like RMSE and MAE.
* **User Interface**: Provides a user-friendly interface for inputting stock symbols and viewing predictions.

## 🛠️ Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/VinayakG311/Trade-Mind.git
   cd Trade-Mind
   ```



2. **Create a Virtual Environment** (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```



3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```



## 🔑 API Keys

To access stock data, you'll need to obtain an API key from a stock data provider (e.g., Alpha Vantage), and an API key for the Open Router LLM

1. **Create a `.env` File**:

   In the root directory, create a file named `.env` and add your API key:

   ```env
   ALPHA_VANTAGE_API_KEY="DUI991O7XVBGTYVA"
   OPENROUTER_API_KEY=""
   OPENROUTER_BASE   = "https://openrouter.ai/api/v1"
   ```



2. **Ensure `.env` is in `.gitignore`**:

   To prevent accidental commits of sensitive information, ensure your `.gitignore` includes:

   ```gitignore
   .env
   ```

