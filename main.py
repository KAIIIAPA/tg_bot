import telebot

from additional_material import TOKEN
from bot_handlers.handlers import send_welcome, handle_photo, callback_query, mirror_callback

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def message_welcome(message):
    send_welcome(bot, message)

@bot.message_handler(content_types=['photo'])
def handle_photo_message(message):
    handle_photo(bot, message)

@bot.callback_query_handler(func=lambda call: call.data in ['pixelate', 'ascii', 'invert', 'mirror', 'heatmap'])
def callback_query_message(call):
    callback_query(bot, call)

@bot.callback_query_handler(func=lambda call: call.data in ["horizontal", "vertical"])
def mirror_callback_message(call):
    mirror_callback(bot, call)


bot.polling(none_stop=True)
