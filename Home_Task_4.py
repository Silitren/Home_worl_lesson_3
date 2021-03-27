#Task_3


def my_func(x, y):
    """
    Функция возводит число x в степень y
    :param x: float
    :param y: integer
    :return: x ** y
    """
    return x ** y


def my_func2(x, y):
    """
    Функция возводит число x в отрицательную степень y
    Не испольхует встроенную функцию **
    :param x: float
    :param y: integer
    :return: c
    """
    z = 1 / x
    c = 1
    for el in range(y):
        c = c * z
        # print(el, range(y), c)
    return c


print(f"Ваш результат: {my_func(float(input('Введите число: ')), int(input('Введите отрицательную степнь: ')))}")
print(f"Ваш результат: {my_func2(float(input('Введите число: ')), abs(int(input('Введите отрицательную степнь: '))))}")
