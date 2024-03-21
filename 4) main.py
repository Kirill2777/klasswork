#coding: utf-8
#Задача 4
import math
def circle_area(radius):
    return math.pi * (radius ** 2)
def square_area(side):
    return side ** 2
a = int(input("Введите сторону квадрата "))
b = int(input("Введите радиус круга "))
circle_area = circle_area(a)
square_area = square_area(b)
if circle_area > square_area:
    print("Квадрат не вписывается в круг ")
elif circle_area < square_area:
    print("Круг не вписывается в квадрат ")
else:
    print("Квадрат и круг имеют одинаковую площадь ")