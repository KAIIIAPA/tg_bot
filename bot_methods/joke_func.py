import random
from additional_material import JOKES


def joke_mes_func():
    """
    Функция для отправки случайной шутки пользователю.
    :return: Случайная шутка отправляется пользователю
    """
    # Выбираем случайную шутку из списка
    joke = random.choice(JOKES)
    return f"Случайная шутка: {joke}"
