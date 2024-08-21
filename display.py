"""
Display module for portfolio visualization
"""
import os
import time
from datetime import datetime

class PortfolioDisplay:
    @staticmethod
    def clear_screen():
        """Clear terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    @staticmethod
    def display_portfolio(portfolio_data):
        """
        Display portfolio in a formatted table
        """
        if not portfolio_data:
            print("No portfolio data available")
            return
        
        holdings = portfolio_data['holdings']
        summary = portfolio_data['summary']
        
        print("=" * 100)
        print(f"CRYPTO PORTFOLIO TRACKER - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 100)
        print(f"{'Coin':<8} {'Amount':<12} {'Buy Price':<12} {'Current Price':<15} {'Invested':<12} {'Current Value':<15} {'P/L':<12} {'P/L %':<10}")
        print("-" * 100)
        
        for holding in holdings:
            # Color coding for profit/loss
            pl_color = "\033[92m" if holding['profit_loss'] >= 0 else "\033[91m"  # Green for profit, red for loss
            reset_color = "\033[0m"
            
            print(f"{holding['symbol']:<8} "
                  f"{holding['amount']:<12.4f} "
                  f"${holding['buy_price']:<11.2f} "
                  f"${holding['current_price']:<14.2f} "
                  f"${holding['invested_value']:<11.2f} "
                  f"${holding['current_value']:<14.2f} "
                  f"{pl_color}${holding['profit_loss']:<11.2f}{reset_color} "
                  f"{pl_color}{holding['profit_loss_percent']:<9.2f}%{reset_color}")
        
        print("-" * 100)
        
        # Summary with color coding
        total_pl_color = "\033[92m" if summary['total_profit_loss'] >= 0 else "\033[91m"
        
        print(f"{'TOTAL':<8} {'':<12} {'':<12} {'':<15} "
              f"${summary['total_invested']:<11.2f} "
              f"${summary['total_current']:<14.2f} "
              f"{total_pl_color}${summary['total_profit_loss']:<11.2f}\033[0m "
              f"{total_pl_color}{summary['total_profit_loss_percent']:<9.2f}%\033[0m")
        print("=" * 100)