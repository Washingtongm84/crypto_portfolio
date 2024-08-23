"""
Main application file for cryptocurrency portfolio tracker
"""
import time
import signal
import sys
from portfolio_manager import PortfolioManager
from display import Display
from config import REFRESH_INTERVAL

class CryptoTracker:
    def __init__(self):
        self.portfolio_manager = PortfolioManager()
        self.running = True
        
        # Setup signal handler for graceful shutdown
        signal.signal(signal.SIGINT, self.signal_handler)
    
    def signal_handler(self, signum, frame):
        """Handle Ctrl+C gracefully"""
        print(f"\n{Fore.YELLOW}Shutting down portfolio tracker...{Style.RESET_ALL}")
        self.running = False
        sys.exit(0)
    
    def run(self):
        """Main application loop"""
        print(f"{Fore.GREEN}Starting Cryptocurrency Portfolio Tracker...{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Press Ctrl+C to exit{Style.RESET_ALL}")
        
        while self.running:
            try:
                Display.clear_screen()
                
                # Update and display portfolio
                portfolio_data = self.portfolio_manager.update_portfolio()
                if portfolio_data:
                    Display.print_portfolio(portfolio_data)
                
                # Wait for next update
                print(f"\n{Fore.CYAN}Next update in {REFRESH_INTERVAL} seconds...{Style.RESET_ALL}")
                time.sleep(REFRESH_INTERVAL)
                
            except KeyboardInterrupt:
                self.signal_handler(None, None)
            except Exception as e:
                print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
                time.sleep(REFRESH_INTERVAL)

if __name__ == "__main__":
    tracker = CryptoTracker()
    tracker.run()