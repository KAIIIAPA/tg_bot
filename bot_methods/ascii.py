from additional_material import ASCII_CHARS, user_states
import io
from PIL import Image

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

def next_ascii_and_send(message, call, bot):
    """
    :param message: Сообщение от пользователя (набор символов).
    :param call: Сообщение от пользователя (картинка).
    :return: Возвращает результат функции ascii_and_send(message, simbols)
    """
    simbols = message.text
    bot.send_message(call.message.chat.id, "Converting your image to ASCII art...")
    ascii_and_send(call.message, simbols, bot)

def ascii_and_send(message, simbols, bot):
    """
    Функция, которая преобразует изображение в ASCII-арт и отправляет результат в виде текстового сообщения.
    :param bot: Bot.
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
