## Cryptocurrency Portfolio Tracker

A simple Python script to track your cryptocurrency portfolio with real-time prices.

### Features
- Real-time price updates from CoinGecko API
- Portfolio performance tracking (profit/loss)
- Colored terminal display
- Auto-refresh every 60 seconds
- Support for multiple cryptocurrencies

### Setup Instructions

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure Your Portfolio:**
   Edit `config.py` and update the `PORTFOLIO` dictionary with your holdings:
   ```python
   PORTFOLIO = {
       "bitcoin": {"amount": 0.5, "purchase_price": 45000},
       "ethereum": {"amount": 3.2, "purchase_price": 3200},
       # Add more coins as needed
   }
   ```

3. **Run the Application:**
   ```bash
   python main.py
   ```

### Usage
- The application will automatically refresh every 60 seconds
- Press `Ctrl+C` to exit the application
- Green numbers indicate profit, red numbers indicate loss

### Customization
- Change refresh interval in `config.py` (REFRESH_INTERVAL)
- Add/remove cryptocurrencies from your portfolio
- Modify display colors in `display.py`

### Supported Cryptocurrencies
Use CoinGecko API coin IDs (e.g., "bitcoin", "ethereum", "cardano", "solana")

### Dependencies
- `requests` - For API calls
- `colorama` - For colored terminal output

### Notes
- Requires internet connection for real-time price updates
- Free tier of CoinGecko API has rate limits
- Data is for informational purposes only