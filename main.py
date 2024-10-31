import telebot
from PIL import Image, ImageOps
import io
from telebot import types

TOKEN = '7520814526:AAG74XNZox0OvVLSf4mFeVcxdqHvUz-YJk4'
bot = telebot.TeleBot(TOKEN)

user_states = {}  # тут будем хранить информацию о действиях пользователя

# набор символов из которых составляем изображение
ASCII_CHARS = '@%#*+=-:. '


def resize_image(image, new_width=100):
    """
    Изменяет размер изображения с сохранением пропорций.
    :param image: Изображение.
    :param new_width: Размер изображения
    :return: Обработанное изображение.
    """
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    return image.resize((new_width, new_height))


def grayify(image):
    """
    Преобразует цветное изображение в оттенки серого.
    :param image: Изображение.
    :return: Обработанное изображение.
    """
    return image.convert("L")


def image_to_ascii(image_stream, simbols, new_width=40):
    """
    Основная функция для преобразования изображения в ASCII-арт. Изменяет размер,
    преобразует в градации серого и затем в строку ASCII-символов.
    :param image_stream: Изображение.
    :param simbols: Набор символов.
    :param new_width: Размер изображения.
    :return: Строку ASCII-символов.
    """
    # Переводим в оттенки серого
    image = Image.open(image_stream).convert('L')

    # меняем размер сохраняя отношение сторон
    width, height = image.size
    aspect_ratio = height / float(width)
    new_height = int(
        aspect_ratio * new_width * 0.55)  # 0,55 так как буквы выше чем шире
    img_resized = image.resize((new_width, new_height))

    img_str = pixels_to_ascii(img_resized, simbols)
    img_width = img_resized.width

    max_characters = 4000 - (new_width + 1)
    max_rows = max_characters // (new_width + 1)

    ascii_art = ""
    for i in range(0, min(max_rows * img_width, len(img_str)), img_width):
        ascii_art += img_str[i:i + img_width] + "\n"

    return ascii_art


def pixels_to_ascii(image, simbols):
    """
    Конвертирует пиксели изображения в градациях серого в строку ASCII-символов,
    используя предопределенную строку ASCII_CHARS.
    :param image: Изображение.
    :param simbols: Набор символов.
    :return: Строку ASCII-символов
    """
    if len(simbols) > 0:
        pixels = image.getdata()
        characters = ""
        for pixel in pixels:
            characters += simbols[pixel * len(simbols) // 256]
        return characters

    pixels = image.getdata()
    characters = ""
    for pixel in pixels:
        characters += ASCII_CHARS[pixel * len(ASCII_CHARS) // 256]
    return characters


# Огрубляем изображение
def pixelate_image(image, pixel_size):
    image = image.resize(
        (image.size[0] // pixel_size, image.size[1] // pixel_size),
        Image.NEAREST
    )
    image = image.resize(
        (image.size[0] * pixel_size, image.size[1] * pixel_size),
        Image.NEAREST
    )
    return image


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    """
    Реагирует на команды /start или /help, отправляя приветственное сообщение.
    :param message: Команда /start или /help.
    :return: Приветственное сообщение.
    """
    bot.reply_to(message, "Send me an image, and I'll provide options for you!")


@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    """
    Реагирует на изображения, отправляемые пользователем, и предлагает варианты обработки.
    :param message: Сообщение от пользователя (изображение).
    :return: Отображает инлайн клавиатуру предлагая варианты обработки изображений
    """
    bot.reply_to(message, "I got your photo! Please choose what you'd like to do with it.",
                 reply_markup=get_options_keyboard())
    user_states[message.chat.id] = {'photo': message.photo[-1].file_id}


def get_options_keyboard():
    """
    Создает клавиатуру с кнопками для выбора пользователем, как обработать изображение.
    :return: Возвращает инлайн клавиатуру бота.
    """
    keyboard = types.InlineKeyboardMarkup()
    pixelate_btn = types.InlineKeyboardButton("Pixelate", callback_data="pixelate")
    ascii_btn = types.InlineKeyboardButton("ASCII Art", callback_data="ascii")
    invert_btn = types.InlineKeyboardButton("Invert image", callback_data="invert")
    keyboard.add(pixelate_btn, ascii_btn, invert_btn)
    return keyboard


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    """
    Определяет действия в ответ на выбор пользователем кнопки и вызывает соответствующую функцию обработки.
    :param call: Выбранная кнопка пользователем.
    :return: Вызывает соответствующую функцию для обработки изображения.
    """
    if call.data == "pixelate":
        bot.answer_callback_query(call.id, "Pixelating your image...")
        pixelate_and_send(call.message)
    elif call.data == "ascii":
        msg = bot.send_message(call.message.chat.id,
                               'Введите набор символов, который будет использоваться для '
                               'преобразования изображения в ASCII-арт (Например, "@%#*+=-:. ").')
        bot.register_next_step_handler(msg, next_ascii_and_send, call)
    elif call.data == "invert":
        bot.answer_callback_query(call.id, "Inverting your image...")
        invert_colors(call.message)


def next_ascii_and_send(message, call):
    """
    :param message: Сообщение от пользователя (набор символов).
    :param call: Сообщение от пользователя (картинка).
    :return: Возвращает результат функции ascii_and_send(message, simbols)
    """
    simbols = message.text
    bot.send_message(call.message.chat.id, "Converting your image to ASCII art...")
    ascii_and_send(call.message, simbols)

def ascii_and_send(message, simbols):
    """
    Функция, которая преобразует изображение в ASCII-арт и отправляет результат в виде текстового сообщения.
    :param message: Сообщение от пользователя.
    :param simbols: Набор символов для создания ASCII-арта.
    :return: Возвращает пользователю изображение в виде текстового сообщения (ASCII-арт)
    """
    photo_id = user_states[message.chat.id]['photo']
    file_info = bot.get_file(photo_id)
    downloaded_file = bot.download_file(file_info.file_path)

    image_stream = io.BytesIO(downloaded_file)
    try:
        ascii_art = image_to_ascii(image_stream, simbols)
        bot.send_message(message.chat.id, f"```\n{ascii_art}\n```", parse_mode="MarkdownV2")
    except:
        bot.send_message(message.chat.id, f"Что-то пошло не так попробуйте еще раз!")

def pixelate_and_send(message):
    """
    Функция, которая пикселизирует изображение и отправляет его обратно пользователю.
    :param message: Сообщение от пользователя.
    :return: Обработанное изображение возвращается пользователю
    """
    photo_id = user_states[message.chat.id]['photo']
    file_info = bot.get_file(photo_id)
    downloaded_file = bot.download_file(file_info.file_path)

    image_stream = io.BytesIO(downloaded_file)
    image = Image.open(image_stream)
    pixelated = pixelate_image(image, 20)

    output_stream = io.BytesIO()
    pixelated.save(output_stream, format="JPEG")
    output_stream.seek(0)
    bot.send_photo(message.chat.id, output_stream)

def invert_colors(message):
    """
    Функция, которая инвертирует изображение и отправляет его обратно пользователю.
    :param message: Сообщение пользователя.
    :return: Обработанное изображение возвращается пользователю
    """
    photo_id = user_states[message.chat.id]['photo']
    file_info = bot.get_file(photo_id)
    downloaded_file = bot.download_file(file_info.file_path)

    image_stream = io.BytesIO(downloaded_file)
    image = Image.open(image_stream)

    # Применяем инвертацию цветов
    inverted_image = ImageOps.invert(image)
    output_stream = io.BytesIO()
    inverted_image.save(output_stream, format="JPEG")
    output_stream.seek(0)
    bot.send_photo(message.chat.id, output_stream)


bot.polling(none_stop=True)
