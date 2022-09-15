# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

Number=int(input("Введите число: "))
my_list = []
for i in range(1, Number+1):
    if(Number%i==0):
       my_list.append(i)
print(my_list)      