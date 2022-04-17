#9.	Указав номер четверти прямоугольной системы координат, 
# показать допустимые значения координат для точек этой четверти

numchet = int(input('Введите номер четверти прямоугольной системы координат:')) 
#while (numchet >=1 and numchet<=4):
   # for i in range (1,5):
if numchet>=1 and numchet<=4:
 if numchet == 1:      
  print('x>=0;  y>=0')
 if numchet == 2:
  print('x>=0;  y<0')
 if numchet == 3:
  print('x<0;  y<0')
 if numchet == 4:
  print('x<0;  y>=0')
else:
 print('не верное значение четверти')