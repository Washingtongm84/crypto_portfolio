"""
Portfolio management and calculations
"""
from crypto_api import CryptoAPI
from config import PORTFOLIO, CURRENCY

class PortfolioManager:
    def __init__(self):
        self.api = CryptoAPI()
        self.portfolio = PORTFOLIO
    
    def calculate_portfolio_value(self):
        """
        Calculate current portfolio value and performance
        """
        coin_ids = list(self.portfolio.keys())
        prices = self.api.get_current_prices(coin_ids)
        
        if not prices:
            return None
        
        portfolio_data = []
        total_invested = 0
        total_current = 0
        
        for coin_id, holding in self.portfolio.items():
            if coin_id in prices:
                current_price = prices[coin_id][CURRENCY]
                amount = holding['amount']
                buy_price = holding['buy_price']
                
                invested_value = amount * buy_price
                current_value = amount * current_price
                profit_loss = current_value - invested_value
                profit_loss_percent = (profit_loss / invested_value) * 100
                
                total_invested += invested_value
                total_current += current_value
                
                portfolio_data.append({
                    'symbol': holding['symbol'],
                    'amount': amount,
                    'buy_price': buy_price,
                    'current_price': current_price,
                    'invested_value': invested_value,
                    'current_value': current_value,
                    'profit_loss': profit_loss,
                    'profit_loss_percent': profit_loss_percent
                })
        
        total_profit_loss = total_current - total_invested
        total_profit_loss_percent = (total_profit_loss / total_invested) * 100 if total_invested > 0 else 0
        
        return {
            'holdings': portfolio_data,
            'summary': {
                'total_invested': total_invested,
                'total_current': total_current,
                'total_profit_loss': total_profit_loss,
                'total_profit_loss_percent': total_profit_loss_percent
            }
        }
    
    def add_holding(self, coin_id, symbol, amount, buy_price):
        """
        Add a new cryptocurrency holding to portfolio
        """
        self.portfolio[coin_id] = {
            'symbol': symbol,
            'amount': amount,
            'buy_price': buy_price
        }
    
    def remove_holding(self, coin_id):
        """
        Remove a cryptocurrency holding from portfolio
        """
        if coin_id in self.portfolio:
            del self.portfolio[coin_id]
            return True
        return False