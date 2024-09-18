# Cryptocurrency Portfolio Tracker

A simple Python script to track your cryptocurrency portfolio value and performance with real-time prices.

## Features

- Real-time price updates from CoinGecko API
- Portfolio performance tracking (profit/loss)
- Support for major cryptocurrencies
- Configurable refresh interval
- Portfolio management (add/remove holdings)
- Color-coded profit/loss display

## Installation

1. Ensure you have Python 3.6+ installed
2. Install required dependencies:
```bash
pip install requests
```

## Usage

### Starting the Tracker
```bash
python main.py
```

### Portfolio Management Commands

**View current portfolio:**
```bash
python main.py list
```

**Add a cryptocurrency holding:**
```bash
python main.py add bitcoin 0.5 45000
```

**Remove a cryptocurrency holding:**
```bash
python main.py remove bitcoin
```

### Supported Cryptocurrencies
- bitcoin (BTC)
- ethereum (ETH)
- cardano (ADA)
- solana (SOL)
- ripple (XRP)
- dogecoin (DOGE)
- polkadot (DOT)
- litecoin (LTC)

## Configuration

Edit `config.py` to customize:
- `REFRESH_INTERVAL`: How often to update prices (in seconds)
- `CURRENCY`: Display currency (usd, eur, etc.)
- `SUPPORTED_CRYPTOS`: Add or remove supported cryptocurrencies

## Portfolio Storage

Your portfolio is stored in `portfolio.json`. You can manually edit this file or use the command-line interface.

## Notes

- The script uses the free CoinGecko API (no API key required)
- Prices update every 60 seconds by default
- Portfolio data is saved automatically
- Colors may not display correctly on all terminals

## Troubleshooting

- Ensure you have an active internet connection
- Check that the cryptocurrency ID matches exactly (lowercase)
- Verify portfolio.json is not corrupted (delete it to reset to default)