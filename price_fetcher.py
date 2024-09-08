"""
Real-time price fetching module
"""

import requests
from config import COINGECKO_API_URL, SUPPORTED_CRYPTOS, CURRENCY

class PriceFetcher:
    def __init__(self):
        self.session = requests.Session()
    
    def get_current_prices(self, crypto_ids):
        """Fetch current prices for given cryptocurrency IDs"""
        if not crypto_ids:
            return {}
        
        # Convert to list if single ID provided
        if isinstance(crypto_ids, str):
            crypto_ids = [crypto_ids]
        
        try:
            response = self.session.get(
                COINGECKO_API_URL,
                params={
                    'ids': ','.join(crypto_ids),
                    'vs_currencies': CURRENCY
                },
                timeout=10
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching prices: {e}")
            return {}
    
    def get_all_supported_prices(self):
        """Get prices for all supported cryptocurrencies"""
        return self.get_current_prices(list(SUPPORTED_CRYPTOS.keys()))