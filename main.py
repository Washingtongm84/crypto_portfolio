"""
Main entry point for the cryptocurrency portfolio tracker
"""
import sys
from portfolio_tracker import PortfolioTracker

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "manage":
        from portfolio_manager import main as manager_main
        manager_main()
    else:
        tracker = PortfolioTracker()
        tracker.run_tracker()

if __name__ == "__main__":
    main()