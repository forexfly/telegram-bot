import os
import telebot

TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

# 🔥 ONLY ACTIVE EMAIL
ACTIVE_EMAILS = [
    "adnanbinfurquan7@gmail.com"
]

# START
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
def ask_email(message):
    bot.send_message(
        message.chat.id,
        "Please enter your registered email address."
    )

# NO BUTTON (REFERRAL)
@bot.message_handler(func=lambda message: message.text == "No ❌")
def send_referral(message):
    bot.send_message(
        message.chat.id,
        "You need to open an account first.\n\n"
        "Register here 👇\n"
        "https://my.winprofx.org/register?promo=forexfly\n\n"
        "After opening account, type /start again."
    )

# EMAIL CHECK SYSTEM
@bot.message_handler(func=lambda message: "@" in message.text and "." in message.text)
def check_email(message):
    email = message.text.strip().lower()

    if email in ACTIVE_EMAILS:
        bot.send_message(
            message.chat.id,
            "✅ Account Verified!\n\n"
            "Here is your private channel link:\n"
            "https://t.me/+o6jbl-th1I1jOWM1"
        )
    else:
        bot.send_message(
            message.chat.id,
            "❌ Your account is not active.\n"
            "Please make sure your trading account is activated."
        )

bot.polling()
