#реализуйте алгоритм задания случайных чисел без использования
# втроенного генератора псевдослучайных чисел

import time

def random_number(minimum, maximum):
    now = str(time.time())
    rnd = int (now [::-1][:3:])
    return minimum + rnd*(maximum-minimum)
print(random_number(1,10))

