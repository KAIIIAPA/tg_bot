from additional_material import user_states
from bot_methods.ascii import grayify
import io
from PIL import Image, ImageOps


def image_is_converted_to_heatmap(bot, message):
    """
    Функция, которая преобразует изображение в тепловую карту и отправляет его обратно пользователю.
    :param bot: Bot.
    :param message: Сообщение пользователя.
    :return: Обработанное изображение возвращается пользователю
    """
    photo_id = user_states[message.chat.id]['photo']
    file_info = bot.get_file(photo_id)
    downloaded_file = bot.download_file(file_info.file_path)

    image_stream = io.BytesIO(downloaded_file)
    # Открываем изображение
    image = Image.open(image_stream)
    # Конвертируем изображение в оттенки серого
    grayscale_image = grayify(image)
    # Применяем цветовую схему тепловой карты
    heatmap = ImageOps.colorize(grayscale_image, black='blue', white='red')
    output_stream = io.BytesIO()
    heatmap.save(output_stream, format="JPEG")
    output_stream.seek(0)
    bot.send_photo(message.chat.id, output_stream)

