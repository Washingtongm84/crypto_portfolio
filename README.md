## Cryptocurrency Portfolio Tracker

A simple Python script to track your cryptocurrency portfolio with real-time prices.

### Features
- Real-time price updates from CoinGecko API
- Portfolio performance tracking (profit/loss)
- Detailed view of individual coin performance
- Automatic updates every 5 minutes
- Clean console display

### Setup Instructions

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure Your Portfolio:**
   Edit `config.py` and update the `PORTFOLIO` dictionary with your holdings:
   ```python
   PORTFOLIO = {
       "bitcoin": {"amount": 0.5, "buy_price": 45000},
       "ethereum": {"amount": 3.2, "buy_price": 3200},
       # Add more coins as needed
   }
   ```

3. **Run the Tracker:**
   ```bash
   python main.py
   ```

### How to Use

1. **Add Your Holdings:** Modify the `PORTFOLIO` in `config.py` with your actual cryptocurrency holdings
2. **Customize Settings:** Adjust `UPDATE_INTERVAL` for how often prices refresh
3. **Run the Script:** Execute `main.py` to start tracking
4. **Monitor:** The script will display your portfolio performance and update automatically

### File Structure
- `config.py` - Configuration and portfolio data
- `crypto_api.py` - API handler for fetching prices
- `portfolio_manager.py` - Portfolio calculations
- `display.py` - Console display formatting
- `main.py` - Main script to run the tracker
- `requirements.txt` - Python dependencies

### Supported Cryptocurrencies
Use CoinGecko API coin IDs (e.g., "bitcoin", "ethereum", "cardano", "solana", etc.)

### Notes
- Free CoinGecko API has rate limits
- Internet connection required for price updates
- Press Ctrl+C to stop the tracker
- Prices are in USD by default (modify `CURRENCY` in config.py for other currencies)