from dotenv import load_dotenv
import os
import telebot
import cryptocompare_api_client as api_cli
import helpers

load_dotenv("secrets.env")
TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["help"])
def handle_help(message: telebot.types.Message):
    bot.reply_to(message, f"To convert currency, type the command /convert , \n "
                          f"symbol of a source currency, followed by the symbol of a destination currency and amount ")

@bot.message_handler(commands=["convert"])
def handle_convert_request(message: telebot.types.Message):
    contents = message.text.upper().split(" ")
    # "command" "USD" "USD" ("1" optional)
    try:
        src_sym = contents[1]
        dst_sym = contents[2]
        if len(contents) >= 4:
            amount = float(contents[3])
        else:
            amount = 1
    except (TypeError, IndexError):
        bot.reply_to(message, "wrong format, please use /help command for more information ")
        return

    try:
        rate = api_cli.Client.request_pair_rate(src_sym, dst_sym)
    except helpers.Exceptions.ProviderConversionError as e:
        bot.reply_to(message, str(e))
        return

    bot.reply_to(message, str(rate * amount))


bot.polling(non_stop=True)
