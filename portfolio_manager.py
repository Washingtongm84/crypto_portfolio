"""
Portfolio management and calculations
"""
from config import PORTFOLIO, CURRENCY

class PortfolioManager:
    def __init__(self, portfolio_data):
        self.portfolio = portfolio_data
    
    def calculate_portfolio_value(self, current_prices):
        """
        Calculate total portfolio value and individual coin performance
        """
        total_invested = 0
        total_current = 0
        coin_performance = {}
        
        for coin_id, data in self.portfolio.items():
            amount = data["amount"]
            buy_price = data["buy_price"]
            current_price = current_prices.get(coin_id, {}).get(CURRENCY, 0)
            
            invested_value = amount * buy_price
            current_value = amount * current_price
            
            total_invested += invested_value
            total_current += current_value
            
            profit_loss = current_value - invested_value
            profit_loss_percent = (profit_loss / invested_value) * 100 if invested_value > 0 else 0
            
            coin_performance[coin_id] = {
                "amount": amount,
                "buy_price": buy_price,
                "current_price": current_price,
                "invested_value": invested_value,
                "current_value": current_value,
                "profit_loss": profit_loss,
                "profit_loss_percent": profit_loss_percent
            }
        
        portfolio_performance = {
            "total_invested": total_invested,
            "total_current": total_current,
            "total_profit_loss": total_current - total_invested,
            "total_profit_loss_percent": ((total_current - total_invested) / total_invested) * 100 if total_invested > 0 else 0,
            "coin_performance": coin_performance
        }
        
        return portfolio_performance