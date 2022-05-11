# Задайте страку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
#  В качестве символа разделителя использовать пробел.

def StrMinMax(str):
    list1 = str.split(' ')
    min = int(list1[0])
    max = int(list1[0])
    for i in range(len(list1)):
        list1[i] = int(list1[i])
        if list1[i]<min:
            min=list1[i]
        if list1[i]>max:
            max=list1[i]
    print(f'минимум равен {min}, максимум равен {max}')   
a = input('введите строку состоящую из набора чисел, в качестве символа разделителя использовать пробел ')
StrMinMax(a) 

