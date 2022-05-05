# найти сумму чисел списка стоящих на нечетных позициях
List = [4,9,2,7,39,430,211,32,111,777]
def SumNumbers(List):
    summa = 0
    for number in List:
        if number % 2:
            summa += number
    return summa
 
print('Сумма нечетных чисел - ', SumNumbers(List))
