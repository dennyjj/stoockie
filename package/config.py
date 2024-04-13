import os


def get_config():
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
        "token": token,
        "chat_id": chat_id,
        "tickers": list(set(tickers.split(","))),
    }
