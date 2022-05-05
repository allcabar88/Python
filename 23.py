# Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, 
# второй и предпоследний и т.д. 
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15] 

mylist = [8, 2, 7, 4, 4, 4, 4, 8, 4, 2, 6, 9, 10, 10, 7, 10, 8, 10, 2, 6]
import math
def mult_pairs(mylist):
    return [mylist[i] * mylist[-i - 1] for i in range(math.ceil(len(mylist)/2))]

print(mylist)
print(mult_pairs(mylist))