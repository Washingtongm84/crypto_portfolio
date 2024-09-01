## Cryptocurrency Portfolio Tracker

A simple Python script to track your cryptocurrency portfolio with real-time prices using the CoinGecko API.

### Features
- Real-time price updates
- Portfolio performance tracking
- Profit/loss calculations
- Color-coded display
- Auto-refresh functionality

### Setup Instructions

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure your portfolio:**
   Edit `config.py` to add your cryptocurrency holdings:
   ```python
   PORTFOLIO = {
       "bitcoin": {
           "symbol": "BTC",
           "amount": 0.5,        # Amount you own
           "buy_price": 45000.00  # Your purchase price
       },
       # Add more coins...
   }
   ```

3. **Run the application:**
   ```bash
   python main.py
   ```

### Usage

- The script will automatically fetch current prices and display your portfolio
- Prices update every 60 seconds (configurable in `config.py`)
- Press `Ctrl+C` to exit the application

### Adding New Coins

To add new cryptocurrencies, use their CoinGecko ID in the `PORTFOLIO` configuration. You can find coin IDs at: https://api.coingecko.com/api/v3/coins/list

### File Structure

- `config.py` - Configuration and portfolio settings
- `crypto_api.py` - API handler for CoinGecko
- `portfolio_manager.py` - Portfolio calculations and management
- `display.py` - Terminal display formatting
- `main.py` - Main application entry point
- `requirements.txt` - Python dependencies

### Notes

- Free CoinGecko API has rate limits
- Internet connection required for real-time prices
- Prices are in USD by default (configurable)
- Colors may not work on all terminals