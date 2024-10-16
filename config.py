"""
Configuration file for cryptocurrency portfolio tracker
"""

# API Configuration
COINGECKO_API_URL = "https://api.coingecko.com/api/v3/simple/price"

# Portfolio configuration - Add your holdings here
PORTFOLIO = {
    "bitcoin": {"amount": 0.5, "buy_price": 45000},
    "ethereum": {"amount": 3.2, "buy_price": 3200},
    "cardano": {"amount": 1000, "buy_price": 1.2},
    "solana": {"amount": 5, "buy_price": 150},
    "polkadot": {"amount": 50, "buy_price": 25}
}

# Currency for display
CURRENCY = "usd"

# Update interval in seconds (5 minutes)
UPDATE_INTERVAL = 300