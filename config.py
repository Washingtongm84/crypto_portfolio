"""
Configuration file for cryptocurrency portfolio tracker
"""

# API Configuration
COINGECKO_API_URL = "https://api.coingecko.com/api/v3"

# Portfolio Configuration - Add your holdings here
PORTFOLIO = {
    "bitcoin": {"amount": 0.5, "purchase_price": 45000},
    "ethereum": {"amount": 3.2, "purchase_price": 3200},
    "cardano": {"amount": 1000, "purchase_price": 1.2},
    "solana": {"amount": 5, "purchase_price": 150},
}

# Display Configuration
CURRENCY = "usd"
REFRESH_INTERVAL = 60  # seconds