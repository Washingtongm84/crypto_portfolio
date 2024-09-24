"""
Cryptocurrency API handler for fetching real-time prices
"""
import requests
from config import COINGECKO_API_URL, REQUEST_TIMEOUT, SUPPORTED_CRYPTOS, CURRENCY

class CryptoAPI:
    def __init__(self):
        self.base_url = COINGECKO_API_URL
    
    def get_current_prices(self, coin_ids):
        """
        Fetch current prices for multiple cryptocurrencies
        """
        try:
            # Convert coin IDs to string for API call
            ids = ",".join(coin_ids)
            
            url = f"{self.base_url}/simple/price"
            params = {
                'ids': ids,
                'vs_currencies': CURRENCY,
                'include_24hr_change': 'true'
            }
            
            response = requests.get(url, params=params, timeout=REQUEST_TIMEOUT)
            response.raise_for_status()
            
            return response.json()
            
        except requests.exceptions.RequestException as e:
            print(f"Error fetching prices: {e}")
            return {}
    
    def get_coin_id(self, symbol):
        """
        Get CoinGecko coin ID from symbol
        """
        return SUPPORTED_CRYPTOS.get(symbol.lower())
    
    def get_supported_symbols(self):
        """
        Return list of supported cryptocurrency symbols
        """
        return list(SUPPORTED_CRYPTOS.keys())