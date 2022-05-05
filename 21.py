# Напишите программу, которая определит позицию второго 
# вхождения строки в списке либо сообщит, что ее нет



my_list = ["123","qwe","23414","asdfaddsd","123"]
num=(input("введите значение: "))
flag = -1
for i in range(len(my_list)):
    if (my_list[i]==num):
        flag+=1
        if flag==1:
            print (i)
            break
else:
    print(-1)


# my_list = ["123","qwe","23414","asdfaddsd","123"]
# num=(input("введите значение: "))
# list1=[i for i,num in enumerate(my_list)]
# if len(list1)>1:
#     print(list1[1])
# else:
#     print(-1)
