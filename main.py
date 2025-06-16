import telebot

# Токен бота
TOKEN = "8011204669:AAF5kUsBvrK8AJybDtRECjHwY6h5vTmfyYA"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет, я бот по недвижимости!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Вы написали: " + message.text)

print("Бот запущен...")
bot.polling()
