import random
from additional_material import COMPLIMENTS


def compliments_mes_func():
    """
    Функция для отправки случайного комплимента пользователю.
    :return: Случайный комплимент отправляется пользователю
    """
    # Выбираем случайный комплимент из списка
    compliment = random.choice(COMPLIMENTS)
    return f"Случайный комплимент: {compliment}"
