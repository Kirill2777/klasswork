#coding: utf-8
#Задача 8
a = int(input("Введите a = "))
meters_1 = a * 0.45

b = int(input("Введите b = "))
meters_2 = b * 0.45

if meters_1 > meters_2:
    print("Первое расстояние больше")
elif meters_1 < meters_2:
    print("Второе расстояние больше")
else:
    print("Расстояния равны")