# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]


list = [5, 7, 2, 5, 10, 15, 10, 8, 3, 9, 11, 6, 17, 11]

def unic(list):
    a = []
    for i in range(len(list)):
        if list[i] not in list[i+1::] and list[i] not in list[:i-1:]:
            a.append(list[i])
    return a

print(unic(list))

str1=str(unic(list))

with open('out.txt', 'w') as data:
    data.write(str1)