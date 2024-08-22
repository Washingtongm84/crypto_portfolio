"""
Main application file for cryptocurrency portfolio tracker
"""
import time
import sys
from portfolio_manager import PortfolioManager
from display import PortfolioDisplay
from config import REFRESH_INTERVAL

def main():
    """
    Main function to run the portfolio tracker
    """
    portfolio_manager = PortfolioManager()
    display = PortfolioDisplay()
    
    print("Starting Cryptocurrency Portfolio Tracker...")
    print("Press Ctrl+C to exit")
    
    try:
        while True:
            portfolio_data = portfolio_manager.calculate_portfolio_value()
            
            if portfolio_data:
                display.clear_screen()
                display.display_portfolio(portfolio_data)
            else:
                print("Error: Could not fetch portfolio data")
            
            print(f"\nRefreshing in {REFRESH_INTERVAL} seconds...")
            
            # Countdown timer
            for i in range(REFRESH_INTERVAL, 0, -1):
                print(f"\rNext update in {i} seconds...", end="", flush=True)
                time.sleep(1)
            print()
            
    except KeyboardInterrupt:
        print("\n\nPortfolio tracker stopped. Goodbye!")
        sys.exit(0)

if __name__ == "__main__":
    main()