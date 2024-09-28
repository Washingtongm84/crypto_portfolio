"""
Portfolio management class
"""
from crypto_api import CryptoAPI
from config import SUPPORTED_CRYPTOS

class Portfolio:
    def __init__(self):
        self.api = CryptoAPI()
        self.holdings = {}  # Format: {coin_id: {'symbol': 'btc', 'amount': 1.5, 'buy_price': 45000}}
    
    def add_holding(self, symbol, amount, buy_price=None):
        """
        Add a cryptocurrency holding to the portfolio
        """
        coin_id = self.api.get_coin_id(symbol)
        if not coin_id:
            print(f"Error: Symbol '{symbol}' not supported")
            return False
        
        if coin_id in self.holdings:
            print(f"Updating existing holding for {symbol}")
        
        self.holdings[coin_id] = {
            'symbol': symbol.upper(),
            'amount': float(amount),
            'buy_price': float(buy_price) if buy_price else None
        }
        return True
    
    def remove_holding(self, symbol):
        """
        Remove a holding from the portfolio
        """
        coin_id = self.api.get_coin_id(symbol)
        if coin_id in self.holdings:
            del self.holdings[coin_id]
            return True
        return False
    
    def calculate_portfolio_value(self, prices):
        """
        Calculate total portfolio value and individual holding performance
        """
        total_value = 0
        total_cost = 0
        holdings_data = []
        
        for coin_id, holding in self.holdings.items():
            if coin_id in prices:
                current_price = prices[coin_id][list(prices[coin_id].keys())[0]]  # Get price in configured currency
                price_change_24h = prices[coin_id].get('usd_24h_change', 0)
                
                holding_value = holding['amount'] * current_price
                total_value += holding_value
                
                # Calculate profit/loss if buy price is available
                if holding['buy_price']:
                    cost_basis = holding['amount'] * holding['buy_price']
                    total_cost += cost_basis
                    profit_loss = holding_value - cost_basis
                    profit_loss_percent = (profit_loss / cost_basis) * 100 if cost_basis > 0 else 0
                else:
                    cost_basis = None
                    profit_loss = None
                    profit_loss_percent = None
                
                holdings_data.append({
                    'symbol': holding['symbol'],
                    'amount': holding['amount'],
                    'current_price': current_price,
                    'value': holding_value,
                    '24h_change': price_change_24h,
                    'buy_price': holding['buy_price'],
                    'profit_loss': profit_loss,
                    'profit_loss_percent': profit_loss_percent
                })
        
        return {
            'total_value': total_value,
            'total_cost': total_cost,
            'total_profit_loss': total_value - total_cost if total_cost else None,
            'total_profit_loss_percent': ((total_value - total_cost) / total_cost * 100) if total_cost else None,
            'holdings': holdings_data
        }