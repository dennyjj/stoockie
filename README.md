### Stoockie

- a cronjob to get the stock price through telegram bot every day
- deploy on AWS with lambda, eventbridge
- written with python and yfinace

---

#### Use Guide

##### Prerequisites:

- Telegram account
- AWS account

1. First you need to create a bot with Telegram @BotFather
2. Obtain the bot token, and also the chat id by starting to chat with the bot
3. Create `.env` with `.env.example` and put the corresponding variables
4. Run the `stoockie.py` to test the bot message!
