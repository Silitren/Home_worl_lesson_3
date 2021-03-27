#Task_2


def data_input(name, surname, birtday_date, city, email, phone_number):
    """
    Запись данных о пользователе
    :param name: str
    :param surname: str
    :param birtday_date: str
    :param city: str
    :param email: str
    :param phone_number: str
    :return: name, surname, birtday_date, city, email, phone_number]
    """
    return ''.join([name, surname, birtday_date, city, email, phone_number])


name = str(input("Введите ваше имя: "))
surname = str(input("Введите фамилию: "))
while True:
    try:
        birtday_date = int(input("Введите дату рождени: "))
    except ValueError:
        print("Вы ввели неккоректное значение")
    else:
        birtday_date = str(birtday_date)
        break
city = str(input("Введите город проживания: "))
email = str(input("Введите ваш email: "))
phone_number = str(input("Введите ваш телефон: "))
print(f"Данные о пользователе: {data_input(name, surname, birtday_date, city, email, phone_number)}")
