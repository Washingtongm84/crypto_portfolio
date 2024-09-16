"""
Main entry point for the cryptocurrency portfolio tracker
"""

import sys
from portfolio_tracker import PortfolioTracker
from portfolio import Portfolio

def main():
    if len(sys.argv) > 1:
        # Command line interface for portfolio management
        portfolio = Portfolio()
        
        if sys.argv[1] == "add" and len(sys.argv) == 5:
            portfolio.add_holding(sys.argv[2], sys.argv[3], sys.argv[4])
        elif sys.argv[1] == "remove" and len(sys.argv) == 3:
            portfolio.remove_holding(sys.argv[2])
        elif sys.argv[1] == "list":
            holdings = portfolio.get_holdings()
            print("Current portfolio:")
            for crypto, data in holdings.items():
                print(f"  {crypto}: {data['amount']} coins bought at ${data['buy_price']}")
        else:
            print_usage()
    else:
        # Start the real-time tracker
        tracker = PortfolioTracker()
        tracker.run_tracker()

def print_usage():
    print("Usage:")
    print("  python main.py                    - Start real-time portfolio tracker")
    print("  python main.py list               - Show current portfolio")
    print("  python main.py add <crypto> <amount> <buy_price> - Add holding")
    print("  python main.py remove <crypto>    - Remove holding")
    print("\nSupported cryptocurrencies: bitcoin, ethereum, cardano, solana, ripple, dogecoin, polkadot, litecoin")
    print("Example: python main.py add bitcoin 0.5 50000")

if __name__ == "__main__":
    main()