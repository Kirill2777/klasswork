#coding: utf -8
#Задача 11
from math import sqrt
a = int(input("Введите a =  "))
b = int(input("Введите b = "))
average_arithmetic = (a + b) / 2
average_geometric = sqrt(a * b)
print("Среднее арифметическое:", average_arithmetic)
print("Среднее геометрическое:", average_geometric)