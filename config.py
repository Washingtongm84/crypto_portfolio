"""
Configuration file for cryptocurrency portfolio tracker
"""

# API Configuration
COINGECKO_API_URL = "https://api.coingecko.com/api/v3"
REQUEST_TIMEOUT = 10

# Display Configuration
REFRESH_INTERVAL = 60  # seconds
CURRENCY = "usd"

# Supported cryptocurrencies (coin IDs from CoinGecko)
SUPPORTED_CRYPTOS = {
    "btc": "bitcoin",
    "eth": "ethereum",
    "ada": "cardano",
    "dot": "polkadot",
    "sol": "solana",
    "matic": "polygon",
    "avax": "avalanche-2",
    "link": "chainlink",
    "ltc": "litecoin",
    "xrp": "ripple"
}