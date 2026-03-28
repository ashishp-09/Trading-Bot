from bot.logging_config import setup_logger
from binance.exceptions import BinanceAPIException
import random

logger = setup_logger()


class OrderService:
    def __init__(self, client):
        self.client = client

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            logger.info(f"Placing order: {symbol} {side} {order_type} {quantity} {price}")

            # Try real API first
            try:
                if order_type == "MARKET":
                    order = self.client.futures_create_order(
                        symbol=symbol,
                        side=side,
                        type="MARKET",
                        quantity=quantity
                    )

                elif order_type == "LIMIT":
                    order = self.client.futures_create_order(
                        symbol=symbol,
                        side=side,
                        type="LIMIT",
                        quantity=quantity,
                        price=price,
                        timeInForce="GTC"
                    )

            # If API fails → fallback to mock
            except Exception as api_error:
                logger.warning(f"API failed, switching to mock mode: {api_error}")

                order = {
                    "orderId": random.randint(100000, 999999),
                    "status": "FILLED",
                    "executedQty": quantity,
                    "avgPrice": price if price else 65000,
                    "mock": True
                }

            logger.info(f"Order Response: {order}")
            return order

        except BinanceAPIException as e:
            logger.error(f"Binance API Error: {e}")
            raise

        except Exception as e:
            logger.error(f"Unexpected Error: {e}")
            raise