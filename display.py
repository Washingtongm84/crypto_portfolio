"""
Display and formatting utilities
"""
from colorama import Fore, Style, init
import os

# Initialize colorama for cross-platform colored output
init(autoreset=True)

class Display:
    @staticmethod
    def clear_screen():
        """Clear the terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    @staticmethod
    def format_currency(amount):
        """Format currency with proper formatting"""
        return f"${amount:,.2f}"
    
    @staticmethod
    def format_percentage(value):
        """Format percentage with color based on value"""
        color = Fore.GREEN if value >= 0 else Fore.RED
        return f"{color}{value:+.2f}%{Style.RESET_ALL}"
    
    @staticmethod
    def print_portfolio(portfolio_data):
        """Display portfolio in a formatted table"""
        if not portfolio_data:
            return
        
        holdings = portfolio_data['holdings']
        summary = portfolio_data['summary']
        
        print(f"\n{Fore.CYAN}{'='*80}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'CRYPTOCURRENCY PORTFOLIO TRACKER':^80}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'='*80}{Style.RESET_ALL}")
        
        # Header
        print(f"\n{Fore.YELLOW}{'Coin':<12} {'Amount':<12} {'Current Price':<15} {'Current Value':<15} {'P&L':<15} {'P&L %':<10}{Style.RESET_ALL}")
        print("-" * 80)
        
        # Holdings
        for holding in holdings:
            pl_color = Fore.GREEN if holding['profit_loss'] >= 0 else Fore.RED
            print(
                f"{holding['coin']:<12} "
                f"{holding['amount']:<12.4f} "
                f"{Display.format_currency(holding['current_price']):<15} "
                f"{Display.format_currency(holding['current_value']):<15} "
                f"{pl_color}{Display.format_currency(holding['profit_loss']):<15}{Style.RESET_ALL} "
                f"{Display.format_percentage(holding['profit_loss_percent']):<10}"
            )
        
        # Summary
        print("-" * 80)
        total_pl_color = Fore.GREEN if summary['total_profit_loss'] >= 0 else Fore.RED
        print(f"\n{Fore.YELLOW}PORTFOLIO SUMMARY:{Style.RESET_ALL}")
        print(f"Total Invested:    {Display.format_currency(summary['total_invested'])}")
        print(f"Current Value:     {Display.format_currency(summary['total_current_value'])}")
        print(f"Total Profit/Loss: {total_pl_color}{Display.format_currency(summary['total_profit_loss'])} "
              f"({Display.format_percentage(summary['total_profit_loss_percent'])}){Style.RESET_ALL}")
        
        print(f"\n{Fore.CYAN}{'='*80}{Style.RESET_ALL}")