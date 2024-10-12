.md

# Cryptocurrency Portfolio Tracker

A simple Python script to track your cryptocurrency portfolio with real-time prices using the CoinGecko API.

## Features

- Real-time cryptocurrency price tracking
- Portfolio performance calculation (profit/loss)
- 24-hour price change monitoring
- Persistent portfolio storage
- Support for multiple cryptocurrencies

## Installation

1. Ensure you have Python 3.6+ installed
2. Install required dependencies:
```bash
pip install requests
```

## Usage

### 1. Manage Your Portfolio
First, set up your portfolio holdings:
```bash
python main.py manage
```

This will open the portfolio manager where you can:
- Add holdings (symbol, amount, optional buy price)
- Remove holdings
- View current holdings
- See supported cryptocurrencies

### 2. Start Tracking
Once your portfolio is set up, start tracking:
```bash
python main.py
```

The tracker will:
- Display your portfolio with current values
- Show profit/loss if buy prices were provided
- Update prices automatically every 60 seconds
- Save your portfolio automatically when you exit (Ctrl+C)

## Supported Cryptocurrencies

The script currently supports:
- BTC (Bitcoin)
- ETH (Ethereum)
- ADA (Cardano)
- DOT (Polkadot)
- SOL (Solana)
- MATIC (Polygon)
- AVAX (Avalanche)
- LINK (Chainlink)
- LTC (Litecoin)
- XRP (Ripple)

## File Structure

- `config.py` - Configuration settings
- `crypto_api.py` - API handler for CoinGecko
- `portfolio.py` - Portfolio management logic
- `portfolio_tracker.py` - Main tracking application
- `portfolio_manager.py` - Portfolio editing interface
- `main.py` - Entry point
- `portfolio.json` - Portfolio data (auto-generated)

## Configuration

You can modify `config.py` to:
- Change refresh interval (`REFRESH_INTERVAL`)
- Change display currency (`CURRENCY`)
- Add more supported cryptocurrencies (`SUPPORTED_CRYPTOS`)

## Notes

- The script uses the free CoinGecko API (no API key required)
- Internet connection is required for real-time prices
- Portfolio data is saved in `portfolio.json`
- Press Ctrl+C to stop the tracker

## Example Usage

```bash
# First, set up your portfolio
python main.py manage

# Then track your portfolio
python main.py
```

This creates a complete, functional cryptocurrency portfolio tracker that's easy to use and extend!