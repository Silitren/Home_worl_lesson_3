# Task_3


def my_func(x, y, z):
    """
    Возвращает сумму наибольших двух аргументов
    ValueError предусмотрен
    :param x: integer
    :param y: integer
    :param z: integer
    :return:
    """
    if x >= z and y >= z:
        return x + y
    elif y >= x and z >= x:
        return y + z
    else:
        return x + z


while True:
    try:
        print(f"Сумма наибольших двух аргументов равна: {my_func(int(input('Введите первое значение: ')), int(input('Введите второе значение: ')), int(input('Введите третье значение: ')))}")
    except ValueError:
        print("Вы ввекли неккоректное значение")
    else:
        break