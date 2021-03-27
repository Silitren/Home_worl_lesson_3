#Task_1
def treatment(a, b):
    """
    Возвращает результат деления двух чисел
    Учтен ZeroDivisionError и ValueError
    :param a: float
    :param b: float
    :return: a / b
    """
    try:
        a / b
    except ZeroDivisionError:
        print("Делить на ноль нельзя!")
        return
    except ValueError:
        print("Вы ввели текстовое значение")
        return
    return a / b


a = float(input("Введите 1-е число: "))
b = float(input("Введите 2-е число: "))
print(f"Результат деления: {treatment(a, b)}")
