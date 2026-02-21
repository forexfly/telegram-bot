import os
import telebot

TOKEN = os.environ.get("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

# START COMMAND
@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Yes ✅", "No ❌")
    bot.send_message(
        message.chat.id,
        "Have you opened your trading account?",
        reply_markup=markup
    )

# YES BUTTON
@bot.message_handler(func=lambda message: message.text == "Yes ✅")
def ask_mt5(message):
    bot.send_message(
        message.chat.id,
        "Please send your MT5 ID"
    )

# NO BUTTON (REFERRAL LINK)
@bot.message_handler(func=lambda message: message.text == "No ❌")
def send_referral(message):
    bot.send_message(
        message.chat.id,
        "No problem 👍\n\n"
        "To access our private gold signals, you need to open a trading account first.\n\n"
        "Open your account using the link below 👇\n"
        "https://my.winprofx.org/register?promo=forexfly\n\n"
        "After opening your account, type /start again."
    )

# WHEN USER SENDS MT5 ID
@bot.message_handler(func=lambda message: message.text.isdigit())
def send_link(message):
    bot.send_message(
        message.chat.id,
        "Access Approved ✅\n\n"
        "Here is your private channel link:\n"
        "https://t.me/+o6jbl-th1I1jOWM1"
    )

bot.polling()
