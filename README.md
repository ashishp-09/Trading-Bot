# Binance Futures Testnet Trading Bot

## Overview

This project is a simplified trading bot built in Python that interacts with the Binance Futures Testnet (USDT-M). It allows users to place MARKET and LIMIT orders through a command-line interface while maintaining clean code structure, logging, and error handling.

The application is designed with modular components and follows a layered architecture for better readability and maintainability.

---

## Features

* Place **MARKET** and **LIMIT** orders
* Supports both **BUY** and **SELL** sides
* CLI-based input using `argparse`
* Input validation (symbol, side, type, quantity, price)
* Structured code (client, services, validators)
* Logging of:

  * API requests
  * API responses
  * Errors and fallbacks
* Graceful error handling
* Mock fallback system if API fails

---

## Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/yourusername/Trading-Bot.git
cd Trading-Bot
```

### 2. Create virtual environment

```
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file:

```
BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_api_secret
```

---

## Usage

### MARKET Order

```
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### LIMIT Order

```
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 60000
```

---

## Sample Output

```
--- Order Summary ---
Symbol: BTCUSDT
Side: BUY
Type: MARKET
Quantity: 0.001

--- Order Response ---
Order ID: 123456
Status: FILLED
Executed Qty: 0.001
Avg Price: 65000
```

---

## Logging

Logs are stored in:

```
logs/bot.log
```

Logs include:

* Order requests
* API responses
* Errors and fallback triggers

---

## Note on API Execution

Due to intermittent authentication and accessibility issues with the Binance Futures Testnet, a fallback **mock execution mode** has been implemented.

The application first attempts to place a real API order. If the API call fails, it automatically switches to a simulated order execution while preserving the response structure and logging behavior.

---
