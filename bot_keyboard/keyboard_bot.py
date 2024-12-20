from telebot import types

def get_options_keyboard_1():
    """
    Создает клавиатуру с кнопками для выбора пользователем, как обработать изображение.
    :return: Возвращает инлайн клавиатуру бота.
    """
    keyboard = types.InlineKeyboardMarkup()
    pixelate_btn = types.InlineKeyboardButton("Pixelate", callback_data="pixelate")
    ascii_btn = types.InlineKeyboardButton("ASCII Art", callback_data="ascii")
    invert_btn = types.InlineKeyboardButton("Invert image", callback_data="invert")
    mirror_btn = types.InlineKeyboardButton("Mirror image", callback_data="mirror")
    heatmap_btn = types.InlineKeyboardButton("Heat map image", callback_data="heatmap")
    sticker_btn = types.InlineKeyboardButton("Resize image for sticker", callback_data="sticker")
    keyboard.add(pixelate_btn, ascii_btn, invert_btn, mirror_btn, heatmap_btn, sticker_btn)
    return keyboard

def get_options_keyboard_2():
    """
    Создает клавиатуру с кнопками для выбора пользователем, для выбора отражения изображения.
    :return: Возвращает инлайн клавиатуру бота.
    """
    keyboard_m = types.InlineKeyboardMarkup()
    flipped_image_1 = types.InlineKeyboardButton("Horizontal flipped", callback_data="horizontal")
    flipped_image_2 = types.InlineKeyboardButton("Vertical flipped", callback_data="vertical")
    keyboard_m.add(flipped_image_1, flipped_image_2)
    return keyboard_m
