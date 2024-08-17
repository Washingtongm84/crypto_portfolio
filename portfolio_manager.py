"""
Portfolio management and calculations
"""
from crypto_api import CryptoAPI
from config import PORTFOLIO, CURRENCY

class PortfolioManager:
    def __init__(self):
        self.api = CryptoAPI()
        self.portfolio = PORTFOLIO
    
    def calculate_portfolio_value(self, prices):
        """
        Calculate current portfolio value and performance
        """
        total_current_value = 0
        total_invested = 0
        portfolio_data = []
        
        for coin_id, holding in self.portfolio.items():
            current_price = prices.get(coin_id, {}).get(CURRENCY, 0)
            amount = holding["amount"]
            purchase_price = holding["purchase_price"]
            
            current_value = amount * current_price
            invested_value = amount * purchase_price
            profit_loss = current_value - invested_value
            profit_loss_percent = (profit_loss / invested_value) * 100 if invested_value > 0 else 0
            
            total_current_value += current_value
            total_invested += invested_value
            
            portfolio_data.append({
                'coin': coin_id.upper(),
                'amount': amount,
                'current_price': current_price,
                'current_value': current_value,
                'invested_value': invested_value,
                'profit_loss': profit_loss,
                'profit_loss_percent': profit_loss_percent
            })
        
        total_profit_loss = total_current_value - total_invested
        total_profit_loss_percent = (total_profit_loss / total_invested) * 100 if total_invested > 0 else 0
        
        return {
            'holdings': portfolio_data,
            'summary': {
                'total_current_value': total_current_value,
                'total_invested': total_invested,
                'total_profit_loss': total_profit_loss,
                'total_profit_loss_percent': total_profit_loss_percent
            }
        }
    
    def update_portfolio(self):
        """
        Fetch latest prices and calculate portfolio performance
        """
        coin_ids = list(self.portfolio.keys())
        prices = self.api.get_prices(coin_ids)
        
        if not prices:
            print("Failed to fetch prices. Please check your internet connection.")
            return None
        
        return self.calculate_portfolio_value(prices)