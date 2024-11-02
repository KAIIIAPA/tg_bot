from PIL import Image
from additional_material import user_states
import io

def reflected_image_horizontally(bot, message):
    """
    Создает отраженную копию изображения по горизонтали.
    :param bot: Bot.
    :param message: Сообщение от пользователя.
    :return: Отраженную копию изображения по горизонтали.
    """
    photo_id = user_states[message.message.chat.id]['photo']
    file_info = bot.get_file(photo_id)
    downloaded_file = bot.download_file(file_info.file_path)
    image_stream = io.BytesIO(downloaded_file)
    image = Image.open(image_stream)

    # Горизонтальное отражение
    flipped_image = image.transpose(Image.FLIP_LEFT_RIGHT)
    output_stream = io.BytesIO()
    flipped_image.save(output_stream, format="JPEG")
    output_stream.seek(0)
    bot.send_photo(message.message.chat.id, output_stream)
