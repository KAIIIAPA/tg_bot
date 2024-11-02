from additional_material import user_states
from PIL import Image, ImageOps
import io

def invert_colors(bot, message):
    """
    Функция, которая инвертирует изображение и отправляет его обратно пользователю.
    :param bot: Bot.
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
