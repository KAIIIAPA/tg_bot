import random
from additional_material import COIN

def flip_a_coin_func():
    """
    Имитация подбрасывания монетки, случайно выбирая "Орел" или "Решка".
    :return: "Heads" или "Tails".
    """
    # Случайно выбираем "Heads" или "Tails"
    flip = random.choice(COIN)
    return f"{flip}"
