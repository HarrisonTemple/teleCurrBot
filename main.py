import requests.exceptions
from dotenv import load_dotenv
import os
import telebot
import cryptocompare_api_client as api_cli
import helpers

load_dotenv("secrets.env")
TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["currencies"])
def handle_currencies_list(message: telebot.types.Message):
    bot.reply_to(message, helpers.get_readable_currencies())

@bot.message_handler(commands=["help"])
def handle_help(message: telebot.types.Message):
    bot.reply_to(message, f"/convert <from> <to> <amount> , /currencies ")

@bot.message_handler(commands=["convert"])
def handle_convert_request(message: telebot.types.Message):
    contents = message.text.upper().split(" ")
    # ["command", "USD", "USD", ("1" optional), ...]
    try:
        src_sym = contents[1]
        dst_sym = contents[2]
        if src_sym not in helpers.supported_currencies.keys() or dst_sym not in helpers.supported_currencies.keys():
            bot.reply_to(message, "unsupported currency, please check /currencies for the list of supported currencies")
            return

        amount = float(contents[3]) if len(contents) >= 4 else 1
    except (TypeError, IndexError):
        bot.reply_to(message, "wrong format, please use /help command for more information ")
        return

    try:
        rate = api_cli.Client.request_pair_rate(src_sym, dst_sym)
    except helpers.Exceptions.ProviderConversionError as e:
        bot.reply_to(message, str(e))
        return
    except requests.exceptions.HTTPError as e:
        bot.reply_to(message, "provider error: " + str(e))
        return

    bot.reply_to(message, str(rate * amount) + dst_sym)


bot.polling(non_stop=True)
