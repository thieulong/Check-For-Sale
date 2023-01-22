import telepot
import json

with open('config.json') as file:
    config = json.load(file)

telegram_bot_token = config["telegram_bot_token"]

telegram_bot = telepot.Bot(token=telegram_bot_token)

def send_message(user_id, msg):
    telegram_bot.sendMessage(chat_id=user_id, text=msg)
