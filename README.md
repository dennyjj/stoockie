### Stoockie

- a cronjob to get the stock price through telegram bot every day
- deploy on AWS with lambda, eventbridge
- written with python and yfinace

---

#### Use Guide

###### Prerequisites: an Telegram account and an AWS account

1. First you need to create a bot with Telegram @BotFather
2. Obtain the bot token, and also the chat id by starting to chat with the bot
   (reference: https://gist.github.com/nafiesl/4ad622f344cd1dc3bb1ecbe468ff9f8a)
3. Create `.env` with `.env.example` and put the corresponding variables
4. Run the `stoockie.py` to test the bot message!
