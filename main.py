from dotenv import load_dotenv
import os
import telebot
import helpers

load_dotenv("secrets.env")
TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start", "help"])
def handle_help(message: telebot.types.Message):
    bot.reply_to(message, f"Welcome, {message.from_user.first_name}! ")

@bot.message_handler(commands=["convert"])
def handle_convert_request(message: telebot.types.Message):
    contents = message.text.split(" ")
    if len(contents) < 4:
        bot.reply_to(message, "wrong format, please use /help command for more information ")


bot.polling(non_stop=True)
