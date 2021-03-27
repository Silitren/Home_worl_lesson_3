#Task_6
liss1 = list()


def int_func(text):
    """
    Воозвращает слово с прописной первой буквы
    :param text: введеная строка
    :return: text с первой заглваной буквой
    """
    return text.capitalize()


text = input().split()
for el in text:
    liss1.append(int_func(str(el)))
print(" ".join(liss1))