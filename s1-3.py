#3.	Вывести на экран числа от -N до N
n=int(input("Введите число N="))
if n==0:
    (print('введено 0ое значение'))
else:
    for i in range (-n, n+1):
        print(i)
