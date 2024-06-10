import os
from typing import Dict


def get_config() -> Dict[str, str]:
    telegram_base_url = "https://api.telegram.org"

    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if token is None:
        raise ValueError("missing config TELEGRAM_BOT_TOKEN")

    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    if chat_id is None:
        raise ValueError("missing config TELEGRAM_CHAT_ID")

    tickers = os.getenv("TICKERS")
    if tickers is None:
        raise ValueError("missing config TICKERS")

    return {
        "telegram_base_url": telegram_base_url,
        "token": token,
        "chat_id": chat_id,
        "tickers": tickers,
    }
