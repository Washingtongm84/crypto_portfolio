"""
Portfolio management script for adding/removing holdings
"""
import json
from portfolio import Portfolio

def display_menu():
    print("\n=== Portfolio Manager ===")
    print("1. View current holdings")
    print("2. Add holding")
    print("3. Remove holding")
    print("4. View supported cryptocurrencies")
    print("5. Exit")
    return input("Choose an option (1-5): ")

def main():
    portfolio = Portfolio()
    
    # Try to load existing portfolio
    try:
        with open("portfolio.json", "r") as f:
            data = json.load(f)
            for holding in data.get('holdings', []):
                portfolio.add_holding(
                    holding['symbol'],
                    holding['amount'],
                    holding.get('buy_price')
                )
    except FileNotFoundError:
        print("No existing portfolio found. Starting fresh.")
    
    while True:
        choice = display_menu()
        
        if choice == "1":
            # View holdings
            if portfolio.holdings:
                print("\nCurrent Holdings:")
                for coin_id, holding in portfolio.holdings.items():
                    print(f"  {holding['symbol']}: {holding['amount']} coins")
                    if holding['buy_price']:
                        print(f"    Buy Price: ${holding['buy_price']:.2f}")
            else:
                print("\nNo holdings in portfolio.")
        
        elif choice == "2":
            # Add holding
            symbol = input("Enter cryptocurrency symbol (e.g., BTC): ").strip().lower()
            amount = input("Enter amount: ").strip()
            buy_price = input("Enter buy price (optional, press enter to skip): ").strip()
            
            if not amount:
                print("Amount is required!")
                continue
            
            try:
                buy_price = float(buy_price) if buy_price else None
                if portfolio.add_holding(symbol, amount, buy_price):
                    print(f"Successfully added {amount} {symbol.upper()}")
                    # Save portfolio
                    data = {'holdings': list(portfolio.holdings.values())}
                    with open("portfolio.json", "w") as f:
                        json.dump(data, f, indent=2)
                else:
                    print("Failed to add holding.")
            except ValueError:
                print("Invalid amount or price format!")
        
        elif choice == "3":
            # Remove holding
            symbol = input("Enter cryptocurrency symbol to remove: ").strip().lower()
            if portfolio.remove_holding(symbol):
                print(f"Removed {symbol.upper()} from portfolio")
                # Save portfolio
                data = {'holdings': list(portfolio.holdings.values())}
                with open("portfolio.json", "w") as f:
                    json.dump(data, f, indent=2)
            else:
                print(f"Holding {symbol.upper()} not found in portfolio")
        
        elif choice == "4":
            # View supported cryptos
            symbols = portfolio.api.get_supported_symbols()
            print("\nSupported Cryptocurrencies:")
            for i, symbol in enumerate(symbols, 1):
                print(f"  {i}. {symbol.upper()}")
        
        elif choice == "5":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()