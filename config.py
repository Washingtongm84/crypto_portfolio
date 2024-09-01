"""
Configuration file for cryptocurrency portfolio tracker
"""

# API Configuration
COINGECKO_API_URL = "https://api.coingecko.com/api/v3/simple/price"

# Supported cryptocurrencies
SUPPORTED_CRYPTOS = {
    'bitcoin': 'BTC',
    'ethereum': 'ETH', 
    'cardano': 'ADA',
    'solana': 'SOL',
    'ripple': 'XRP',
    'dogecoin': 'DOGE',
    'polkadot': 'DOT',
    'litecoin': 'LTC'
}

# Display settings
CURRENCY = 'usd'
REFRESH_INTERVAL = 60  # seconds