#coding: utf -8
#Задача 15
a = int(input("Введите a = "))
b = int(input("Введите b = "))
c = int(input("Введите c = "))
s = 2 * (a * b + b * c + a * c)
v = a * b * c
print("Площадь поверхности:", s)
print("Объем:", v)