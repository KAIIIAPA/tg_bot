from additional_material import user_states
from bot_methods.ascii import next_ascii_and_send
from bot_methods.invert_image import invert_colors
from bot_methods.pixelate_image import pixelate_and_send
from bot_methods.reflected_image_horizontally import reflected_image_horizontally
from bot_methods.reflected_image_vertically import reflected_image_vertically
from bot_keyboard.keyboard_bot import get_options_keyboard_1, get_options_keyboard_2


def send_welcome(bot, message):
    """
    Реагирует на команды /start или /help, отправляя приветственное сообщение.
    :param bot: Bot
    :param message: Команда /start или /help.
    :return: Приветственное сообщение.
    """
    bot.reply_to(message, "Send me an image, and I'll provide options for you!")

def handle_photo(bot, message):
    """
    Реагирует на изображения, отправляемые пользователем, и предлагает варианты обработки.
    :param bot: Bot.
    :param message: Сообщение от пользователя (изображение).
    :return: Отображает инлайн клавиатуру предлагая варианты обработки изображений
    """
    user_states[message.chat.id] = {'photo': message.photo[-1].file_id}
    bot.reply_to(message, "I got your photo! Please choose what you'd like to do with it.",
                 reply_markup=get_options_keyboard_1())

def callback_query(bot, call):
    """
    Определяет действия в ответ на выбор пользователем кнопки и вызывает соответствующую функцию обработки.
    :param bot: Bot.
    :param call: Выбранная кнопка пользователем.
    :return: Вызывает соответствующую функцию для обработки изображения.
    """
    if call.data == "pixelate":
        bot.answer_callback_query(call.id, "Pixelating your image...")
        pixelate_and_send(bot, call.message)
    elif call.data == "ascii":
        msg = bot.send_message(call.message.chat.id,
                               'Введите набор символов, который будет использоваться для '
                               'преобразования изображения в ASCII-арт (Например, "@%#*+=-:. ").')
        bot.register_next_step_handler(msg, next_ascii_and_send, call, bot)
    elif call.data == "invert":
        bot.answer_callback_query(call.id, "Inverting your image...")
        invert_colors(bot, call.message)
    elif call.data == "mirror":
        bot.reply_to(call.message, "Please select which mirrored copy of the image you would like to make.",
                     reply_markup=get_options_keyboard_2())

def mirror_callback(bot, call):
    """
    Создает отраженную копию изображения по горизонтали или вертикали.
    :param bot: Bot.
    :param call: Сообщение от пользователя.
    :return: Отраженную копию изображения по горизонтали или вертикали.
    """
    try:
        if call.data == 'horizontal':
            bot.answer_callback_query(call.id, "Transposing your image...")
            reflected_image_horizontally(bot, message=call)
        elif call.data == 'vertical':
            bot.answer_callback_query(call.id, "Transposing your image...")
            reflected_image_vertically(bot, message=call)
    except:
        raise ValueError("Направление должно быть либо 'horizontal', либо 'vertical'")