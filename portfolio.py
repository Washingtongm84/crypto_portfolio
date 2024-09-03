"""
Portfolio management module
"""

import json
import os
from config import SUPPORTED_CRYPTOS

class Portfolio:
    def __init__(self, portfolio_file='portfolio.json'):
        self.portfolio_file = portfolio_file
        self.holdings = self.load_portfolio()
    
    def load_portfolio(self):
        """Load portfolio from JSON file or create default"""
        if os.path.exists(self.portfolio_file):
            try:
                with open(self.portfolio_file, 'r') as f:
                    return json.load(f)
            except (json.JSONDecodeError, FileNotFoundError):
                print("Error loading portfolio file. Creating new portfolio.")
                return self.create_default_portfolio()
        else:
            return self.create_default_portfolio()
    
    def create_default_portfolio(self):
        """Create a default portfolio structure"""
        default_portfolio = {
            'bitcoin': {'amount': 0.1, 'buy_price': 45000},
            'ethereum': {'amount': 1.5, 'buy_price': 3000},
            'cardano': {'amount': 1000, 'buy_price': 1.2}
        }
        self.save_portfolio(default_portfolio)
        return default_portfolio
    
    def save_portfolio(self, portfolio_data=None):
        """Save portfolio to JSON file"""
        data = portfolio_data or self.holdings
        with open(self.portfolio_file, 'w') as f:
            json.dump(data, f, indent=2)
    
    def add_holding(self, crypto_id, amount, buy_price):
        """Add a new cryptocurrency holding"""
        if crypto_id not in SUPPORTED_CRYPTOS:
            print(f"Error: {crypto_id} is not supported.")
            return False
        
        self.holdings[crypto_id] = {
            'amount': float(amount),
            'buy_price': float(buy_price)
        }
        self.save_portfolio()
        print(f"Added {amount} {SUPPORTED_CRYPTOS[crypto_id]} at ${buy_price}")
        return True
    
    def remove_holding(self, crypto_id):
        """Remove a cryptocurrency holding"""
        if crypto_id in self.holdings:
            del self.holdings[crypto_id]
            self.save_portfolio()
            print(f"Removed {crypto_id} from portfolio")
            return True
        else:
            print(f"Error: {crypto_id} not found in portfolio")
            return False
    
    def get_holdings(self):
        """Return current holdings"""
        return self.holdings.copy()