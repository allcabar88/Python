#задайте список. Напишите программу, которая определит, 
# присутствует ли в заданом списке некое числои
# a = [1,2,234,234,234,234]
# b = 237
# c=0
# for i in a:
#     if (i==b):
#         c=c+1
# if (c>0):
#     print ('YES')
# else:
#     print ('NO')

# my_list = [1,2,234,234,234,234]
# num= 2
# flag=-1
# for i in range(len(my_list)):
#     if (my_list[i]==num):
#         flag=i
# if flag !=-1:
#     print ('YES', flag)
# else:
#     print ('NO')

my_list = [1,2,234,234,234,234]
num= 2
print (num in my_list)