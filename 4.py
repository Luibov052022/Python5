# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и 
# записать в файл многочлен степени k.
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

k = int(input("Введите степень: "))
import numpy as np
import random as rnd
my_list = []
for i in  range(k+1):
    my_list.append(rnd.randint(0, 100))
with open('file2.txt', 'w') as data:
    data.write(str(np.poly1d(my_list)))
print(np.poly1d(my_list))
