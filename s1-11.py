# 11.	Сформировать список из  N членов последовательности.
#Для N = 5;  1, -3, 9, -27, 81 и т.д.

n=int(input('Введите количество членов N последовательности:'))

numbers = list (range(n))
numbers[0]=1
#print(numbers[0])
for i in range(1, n):
    numbers[i] = numbers[i-1]*(-3)
    #print(numbers[i])
print(numbers)