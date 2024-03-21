#coding: utf-8
#Задача 13
import math
x = int(input("Введите x = "))
y = int(input("Введите y = "))
arithmetic_mean = (x + y) / 2
geometric_mean = math.sqrt(x * y)
print("Среднее арифметическое: ", arithmetic_mean)
print("Среднее геометрическое: ", geometric_mean)