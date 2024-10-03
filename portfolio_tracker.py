"""
Main portfolio tracker application
"""
import time
import json
import os
from portfolio import Portfolio
from config import REFRESH_INTERVAL, CURRENCY

class PortfolioTracker:
    def __init__(self, portfolio_file="portfolio.json"):
        self.portfolio = Portfolio()
        self.portfolio_file = portfolio_file
        self.load_portfolio()
    
    def load_portfolio(self):
        """
        Load portfolio from JSON file
        """
        if os.path.exists(self.portfolio_file):
            try:
                with open(self.portfolio_file, 'r') as f:
                    data = json.load(f)
                    for holding in data.get('holdings', []):
                        self.portfolio.add_holding(
                            holding['symbol'],
                            holding['amount'],
                            holding.get('buy_price')
                        )
                print(f"Portfolio loaded from {self.portfolio_file}")
            except Exception as e:
                print(f"Error loading portfolio: {e}")
    
    def save_portfolio(self):
        """
        Save portfolio to JSON file
        """
        try:
            data = {'holdings': list(self.portfolio.holdings.values())}
            with open(self.portfolio_file, 'w') as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            print(f"Error saving portfolio: {e}")
    
    def display_portfolio(self, portfolio_data):
        """
        Display portfolio in a formatted way
        """
        print("\n" + "="*80)
        print(f"{'CRYPTO PORTFOLIO TRACKER':^80}")
        print("="*80)
        
        print(f"\n{'Symbol':<8} {'Amount':<12} {'Current Price':<15} {'Value':<15} {'24h Change':<12} {'P/L':<15} {'P/L %':<10}")
        print("-"*80)
        
        for holding in portfolio_data['holdings']:
            # Format values
            amount = f"{holding['amount']:.6f}"
            current_price = f"${holding['current_price']:.2f}"
            value = f"${holding['value']:.2f}"
            change_24h = f"{holding['24h_change']:.2f}%"
            
            # Format profit/loss
            if holding['profit_loss'] is not None:
                pl_sign = "+" if holding['profit_loss'] >= 0 else ""
                pl = f"{pl_sign}${holding['profit_loss']:.2f}"
                pl_percent = f"{pl_sign}{holding['profit_loss_percent']:.2f}%"
            else:
                pl = "N/A"
                pl_percent = "N/A"
            
            print(f"{holding['symbol']:<8} {amount:<12} {current_price:<15} {value:<15} {change_24h:<12} {pl:<15} {pl_percent:<10}")
        
        # Display totals
        print("-"*80)
        print(f"{'TOTAL VALUE:':<20} ${portfolio_data['total_value']:.2f}")
        
        if portfolio_data['total_profit_loss'] is not None:
            pl_sign = "+" if portfolio_data['total_profit_loss'] >= 0 else ""
            print(f"{'TOTAL P/L:':<20} {pl_sign}${portfolio_data['total_profit_loss']:.2f}")
            print(f"{'TOTAL P/L %:':<20} {pl_sign}{portfolio_data['total_profit_loss_percent']:.2f}%")
        
        print(f"{'Last Updated:':<20} {time.strftime('%Y-%m-%d %H:%M:%S')}")
        print("="*80)
    
    def run_tracker(self):
        """
        Main tracking loop
        """
        print("Starting Cryptocurrency Portfolio Tracker...")
        print("Press Ctrl+C to stop tracking")
        
        try:
            while True:
                # Get current prices
                coin_ids = list(self.portfolio.holdings.keys())
                if coin_ids:
                    prices = self.portfolio.api.get_current_prices(coin_ids)
                    portfolio_data = self.portfolio.calculate_portfolio_value(prices)
                    self.display_portfolio(portfolio_data)
                else:
                    print("\nNo holdings in portfolio. Use the management script to add holdings.")
                
                print(f"\nRefreshing in {REFRESH_INTERVAL} seconds...")
                time.sleep(REFRESH_INTERVAL)
                
        except KeyboardInterrupt:
            print("\n\nStopping portfolio tracker...")
            self.save_portfolio()