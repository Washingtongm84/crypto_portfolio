"""
Display module for showing portfolio performance
"""
from datetime import datetime

class Display:
    @staticmethod
    def format_currency(amount):
        """Format currency with 2 decimal places"""
        return f"${amount:,.2f}"
    
    @staticmethod
    def format_percentage(value):
        """Format percentage with 2 decimal places"""
        return f"{value:+.2f}%"
    
    def show_portfolio_summary(self, performance):
        """Display portfolio summary"""
        print("\n" + "="*60)
        print(f"PORTFOLIO SUMMARY - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("="*60)
        
        print(f"Total Invested: {self.format_currency(performance['total_invested'])}")
        print(f"Current Value:  {self.format_currency(performance['total_current'])}")
        print(f"Profit/Loss:    {self.format_currency(performance['total_profit_loss'])} "
              f"({self.format_percentage(performance['total_profit_loss_percent'])})")
        
        # Color code based on profit/loss
        if performance['total_profit_loss'] >= 0:
            print("💰 Portfolio is in PROFIT")
        else:
            print("📉 Portfolio is in LOSS")
    
    def show_detailed_view(self, performance):
        """Display detailed view of each coin"""
        print("\n" + "-"*80)
        print("DETAILED HOLDINGS")
        print("-"*80)
        print(f"{'Coin':<12} {'Amount':<10} {'Buy Price':<12} {'Current':<12} {'Invested':<12} {'Current Val':<12} {'P/L':<12} {'P/L %':<10}")
        print("-"*80)
        
        for coin_id, data in performance['coin_performance'].items():
            coin_display = coin_id.capitalize()
            print(f"{coin_display:<12} {data['amount']:<10.4f} "
                  f"{self.format_currency(data['buy_price']):<12} "
                  f"{self.format_currency(data['current_price']):<12} "
                  f"{self.format_currency(data['invested_value']):<12} "
                  f"{self.format_currency(data['current_value']):<12} "
                  f"{self.format_currency(data['profit_loss']):<12} "
                  f"{self.format_percentage(data['profit_loss_percent']):<10}")