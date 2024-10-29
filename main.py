"""
Main script to run the cryptocurrency portfolio tracker
"""
import time
import sys
from config import PORTFOLIO, UPDATE_INTERVAL
from crypto_api import CryptoAPI
from portfolio_manager import PortfolioManager
from display import Display

def main():
    # Initialize components
    api = CryptoAPI()
    portfolio_manager = PortfolioManager(PORTFOLIO)
    display = Display()
    
    print("🚀 Cryptocurrency Portfolio Tracker Started!")
    print("Press Ctrl+C to stop the tracker\n")
    
    try:
        while True:
            # Fetch current prices
            current_prices = api.get_portfolio_prices(PORTFOLIO)
            
            if current_prices:
                # Calculate portfolio performance
                performance = portfolio_manager.calculate_portfolio_value(current_prices)
                
                # Display results
                display.show_portfolio_summary(performance)
                display.show_detailed_view(performance)
                
                print(f"\n⏰ Next update in {UPDATE_INTERVAL//60} minutes...")
                print("-"*60)
                
            else:
                print("❌ Failed to fetch prices. Retrying...")
            
            # Wait for next update
            time.sleep(UPDATE_INTERVAL)
            
    except KeyboardInterrupt:
        print("\n\n👋 Portfolio tracker stopped. Goodbye!")
        sys.exit(0)

if __name__ == "__main__":
    main()