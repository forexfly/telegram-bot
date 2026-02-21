import os
import telebot

TOKEN = os.environ.get("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Yes ✅", "No ❌")
    bot.send_message(message.chat.id,
                     "Have you opened your trading account?",
                     reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "Yes ✅")
def ask_mt5(message):
    bot.send_message(message.chat.id, "Please send your MT5 ID")

@bot.message_handler(func=lambda message: message.text.isdigit())
def send_link(message):
    bot.send_message(message.chat.id,
                     "Access Approved ✅\nHere is your private channel link:\nhttps://t.me/+o6jbl-th1I1jOWM1")

bot.polling()
