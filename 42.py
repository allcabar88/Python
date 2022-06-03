# Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных.
# входные и выходные данные хранятся в отдельных текстовых файлах

with open('in.txt', 'r') as data:
    data1 = data.read()
    
def encode(ss):
    str_code = ''
    prev_char = ''
    count = 1
    for char in ss:
        if char != prev_char:
            if prev_char:
                str_code += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    return str_code


str_code = encode(data1)
print(str_code)

with open('Out.txt', 'w') as data2:
    data2.write(str_code)
with open('Out.txt', 'r') as data:
    data3 = data.read()


def decoding(ss:str):
    count = ''
    str_decode = ''
    for char in ss:
        if char.isdigit():
            count += char 
        else:
            str_decode += char * int(count)
            count = ''
    return str_decode

str_decode = decoding(data3)
print(str_decode)
