from additional_material import user_states
from PIL import Image
import io

def resize_for_sticker(bot, message, max_size=512):
    """
    Функция, которая изменяет размер изображения для стикера и отправляет его обратно пользователю.
    :param bot: Bot.
    :param message: Сообщение пользователя.
    :param max_size: Максимальная сторона в данном случае 512 пикселей.
    :return: Обработанное изображение возвращается пользователю.
    """
    photo_id = user_states[message.chat.id]['photo']
    file_info = bot.get_file(photo_id)
    downloaded_file = bot.download_file(file_info.file_path)
    image_stream = io.BytesIO(downloaded_file)
    image = Image.open(image_stream)
    width, height = image.size

    # Проверяем, нужно ли изменять размеры
    if max(width, height) <= max_size:
        output_stream = io.BytesIO()
        image.save(output_stream, format="JPEG")
        output_stream.seek(0)
        bot.send_photo(message.chat.id, output_stream)

    else:
        # Вычисляем новый размер, сохраняя пропорции
        scale_factor = max_size / max(width, height)
        new_width = int(width * scale_factor)
        new_height = int(height * scale_factor)

        # Изменяем размер изображения
        resized_img = image.resize((new_width, new_height), resample=Image.LANCZOS)
        output_stream = io.BytesIO()
        resized_img.save(output_stream, format="JPEG")
        output_stream.seek(0)
        bot.send_photo(message.chat.id, output_stream)
