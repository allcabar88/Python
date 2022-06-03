# Напишите программу, удаляющую из текста все слова содержащие "абв"

text=(input("введите текст: "))

def del_words(text):
    text = list(filter(lambda x: 'абв' not in x, text.split()))
    return " ".join(text)

text = del_words(text)
print(text)