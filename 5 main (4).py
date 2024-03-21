#coding: utf-8
#Задача 10
import math
a = int(input("Введите  a = "))
b = int(input("Введите  b = "))
h = int(input("Введите  h = "))
c = math.sqrt(h * h + ((a - b) / 2) * ((a - b) / 2))
perimeter = a + b + c * 2
print("Периметр равнобедренной трапеции:", perimeter)