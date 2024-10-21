"""
Cryptocurrency API handler for fetching real-time prices
"""
import requests
from config import COINGECKO_API_URL, CURRENCY

class CryptoAPI:
    def __init__(self):
        self.base_url = COINGECKO_API_URL
    
    def get_prices(self, coin_ids):
        """
        Fetch current prices for given coin IDs
        """
        try:
            # Convert list to comma-separated string
            ids = ",".join(coin_ids)
            
            params = {
                'ids': ids,
                'vs_currencies': CURRENCY
            }
            
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            
            return response.json()
            
        except requests.exceptions.RequestException as e:
            print(f"Error fetching prices: {e}")
            return {}
    
    def get_portfolio_prices(self, portfolio):
        """
        Get prices for all coins in portfolio
        """
        coin_ids = list(portfolio.keys())
        return self.get_prices(coin_ids)