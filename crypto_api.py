"""
Cryptocurrency API handler for fetching real-time prices
"""
import requests
from config import COINGECKO_API_URL, CURRENCY

class CryptoAPI:
    def __init__(self):
        self.base_url = COINGECKO_API_URL
    
    def get_current_prices(self, coin_ids):
        """
        Fetch current prices for multiple cryptocurrencies
        """
        try:
            # Convert list to comma-separated string
            ids = ",".join(coin_ids)
            
            url = f"{self.base_url}/simple/price"
            params = {
                'ids': ids,
                'vs_currencies': CURRENCY
            }
            
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            
            return response.json()
            
        except requests.exceptions.RequestException as e:
            print(f"Error fetching prices: {e}")
            return {}
    
    def get_coin_list(self):
        """
        Get list of supported cryptocurrencies
        """
        try:
            url = f"{self.base_url}/coins/list"
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching coin list: {e}")
            return []