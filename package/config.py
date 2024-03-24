import os


def get_config():
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if token is None:
        raise ValueError("missing config TELEGRAM_BOT_TOKEN")

    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    if chat_id is None:
        raise ValueError("missing config TELEGRAM_CHAT_ID")

    ticker_one = os.getenv("TICKER_ONE")
    if ticker_one is None:
        raise ValueError("missing config TICKER_ONE")

    ticker_two = os.getenv("TICKER_TWO")
    if ticker_two is None:
        raise ValueError("missing config TICKER_TWO")

    ticker_three = os.getenv("TICKER_THREE")
    if ticker_three is None:
        raise ValueError("missing config TICKER_THREE")

    return {
        'token': token,
        'chat_id': chat_id,
        'ticker_one': ticker_one,
        'ticker_two': ticker_two,
        'ticker_three': ticker_three,
    }
