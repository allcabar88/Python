#2.	Найти максимальное из пяти чисел
a= int(input('Введите число a='))
b= int(input('Введите число b='))
c= int(input('Введите число c='))
d= int(input('Введите число d='))
f= int(input('Введите число f='))

mx = a
if b > mx:
    mx = b
if c > mx:
    mx = c
if d > mx:
    mx = d
if f > mx:
    mx = f
print(mx)