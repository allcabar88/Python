# В файле находится N натуральных чисел, 
# записанных через пробел. Среди чисел не 
# хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.

data=open(r'E:\ucheba\python\lection 1\35\filenum.txt','r' ) 
a=data.readline().split()

for i in range(len(a)):
    a[i]=int(a[i])
for j in range(1,len(a)):
    if a[j] - 1 == a[j - 1]:
        continue
    else:
        print(a[j]-1)
    
