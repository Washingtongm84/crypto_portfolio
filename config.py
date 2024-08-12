"""
Configuration file for cryptocurrency portfolio tracker
"""

# API Configuration
COINGECKO_API_URL = "https://api.coingecko.com/api/v3"

# Portfolio configuration - Add your holdings here
PORTFOLIO = {
    "bitcoin": {
        "symbol": "BTC",
        "amount": 0.5,
        "buy_price": 45000.00
    },
    "ethereum": {
        "symbol": "ETH", 
        "amount": 2.0,
        "buy_price": 3200.00
    },
    "cardano": {
        "symbol": "ADA",
        "amount": 1000.0,
        "buy_price": 1.20
    }
}

# Display configuration
CURRENCY = "usd"
REFRESH_INTERVAL = 60  # seconds