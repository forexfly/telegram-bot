import os
import telebot

TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

# ✅ ONLY ACTIVE EMAIL
ACTIVE_EMAILS = [
    "adnanbinfurquan7@gmail.com"
]

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

# YES BUTTON → ASK EMAIL
@bot.message_handler(func=lambda message: message.text == "Yes ✅")
def ask_email(message):
    bot.send_message(
        message.chat.id,
        "Please enter your registered email address."
    )

# NO BUTTON → REFERRAL LINK
@bot.message_handler(func=lambda message: message.text == "No ❌")
def send_referral(message):
    bot.send_message(
        message.chat.id,
        "To access our private gold signals, you must open a trading account first.\n\n"
        "Register using the link below 👇\n"
        "https://my.winprofx.org/register?promo=forexfly\n\n"
        "After opening your account, type /start again."
    )

# EMAIL VERIFICATION SYSTEM
@bot.message_handler(func=lambda message: "@" in message.text and "." in message.text)
def check_email(message):
    email = message.text.strip().lower()

    if email in ACTIVE_EMAILS:
        bot.send_message(
            message.chat.id,
            "✅ Account Verified Successfully!\n\n"
            "Here is your private channel access link 👇\n"
            "https://t.me/+o6jbl-th1I1jOWM1"
        )
    else:
        bot.send_message(
            message.chat.id,
            "❌ Your account is not active.\n\n"
            "To get access, your trading account must be:\n"
            "• Fully activated ✅\n"
            "• Have active trades running 📊\n\n"
            "Once your account is active and trades are open, type /start again."
        )

bot.polling()
