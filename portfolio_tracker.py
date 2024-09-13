"""
Main portfolio tracker application
"""

import time
import os
from portfolio import Portfolio
from price_fetcher import PriceFetcher
from config import SUPPORTED_CRYPTOS, CURRENCY, REFRESH_INTERVAL

class PortfolioTracker:
    def __init__(self):
        self.portfolio = Portfolio()
        self.price_fetcher = PriceFetcher()
    
    def calculate_performance(self, holdings, prices):
        """Calculate portfolio performance metrics"""
        total_invested = 0
        total_current = 0
        performance_data = {}
        
        for crypto_id, holding in holdings.items():
            if crypto_id in prices:
                current_price = prices[crypto_id][CURRENCY]
                amount = holding['amount']
                buy_price = holding['buy_price']
                
                invested = amount * buy_price
                current_value = amount * current_price
                profit_loss = current_value - invested
                profit_loss_percent = (profit_loss / invested) * 100 if invested > 0 else 0
                
                total_invested += invested
                total_current += current_value
                
                performance_data[crypto_id] = {
                    'symbol': SUPPORTED_CRYPTOS.get(crypto_id, crypto_id.upper()),
                    'amount': amount,
                    'buy_price': buy_price,
                    'current_price': current_price,
                    'invested': invested,
                    'current_value': current_value,
                    'profit_loss': profit_loss,
                    'profit_loss_percent': profit_loss_percent
                }
        
        total_profit_loss = total_current - total_invested
        total_profit_loss_percent = (total_profit_loss / total_invested) * 100 if total_invested > 0 else 0
        
        return {
            'holdings': performance_data,
            'summary': {
                'total_invested': total_invested,
                'total_current': total_current,
                'total_profit_loss': total_profit_loss,
                'total_profit_loss_percent': total_profit_loss_percent
            }
        }
    
    def display_portfolio(self, performance_data):
        """Display portfolio in a formatted way"""
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print("=" * 80)
        print("CRYPTOCURRENCY PORTFOLIO TRACKER")
        print("=" * 80)
        print(f"{'Cryptocurrency':<15} {'Amount':<12} {'Avg Buy':<10} {'Current':<10} {'Invested':<12} {'Current Val':<12} {'P/L':<12} {'P/L %':<10}")
        print("-" * 80)
        
        for crypto_id, data in performance_data['holdings'].items():
            color = '\033[92m' if data['profit_loss'] >= 0 else '\033[91m'  # Green for profit, red for loss
            reset = '\033[0m'
            
            print(f"{data['symbol']:<15} {data['amount']:<12.4f} ${data['buy_price']:<9.2f} "
                  f"${data['current_price']:<9.2f} ${data['invested']:<11.2f} "
                  f"${data['current_value']:<11.2f} {color}${data['profit_loss']:<11.2f}{reset} "
                  f"{color}{data['profit_loss_percent']:<9.1f}%{reset}")
        
        print("-" * 80)
        
        summary = performance_data['summary']
        color = '\033[92m' if summary['total_profit_loss'] >= 0 else '\033[91m'
        reset = '\033[0m'
        
        print(f"{'TOTAL':<15} {'':<12} {'':<10} {'':<10} ${summary['total_invested']:<11.2f} "
              f"${summary['total_current']:<11.2f} {color}${summary['total_profit_loss']:<11.2f}{reset} "
              f"{color}{summary['total_profit_loss_percent']:<9.1f}%{reset}")
        print("=" * 80)
        print(f"Last updated: {time.strftime('%Y-%m-%d %H:%M:%S')}")
        print("Press Ctrl+C to exit")
    
    def run_tracker(self):
        """Main tracking loop"""
        print("Starting cryptocurrency portfolio tracker...")
        print("Loading portfolio and fetching prices...")
        
        try:
            while True:
                holdings = self.portfolio.get_holdings()
                prices = self.price_fetcher.get_current_prices(list(holdings.keys()))
                
                if prices:
                    performance_data = self.calculate_performance(holdings, prices)
                    self.display_portfolio(performance_data)
                else:
                    print("Error: Could not fetch price data")
                
                time.sleep(REFRESH_INTERVAL)
                
        except KeyboardInterrupt:
            print("\n\nPortfolio tracker stopped. Goodbye!")