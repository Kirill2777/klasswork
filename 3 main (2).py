#coding: utf-8
#Задача 8
import math
def area_circle(r):
    return math.pi*r**2

def area_ring(r1, r2):
	area1 = area_circle(r1)
	area2 = area_circle(r2)
	average_radius = (r1 + r2) / 2
	middle_area = area_circle(average_radius)
	result = middle_area - (area1 + area2)
	return result if r1 > r2 else -result

r1 = int(input("Введите r1 = "))
r2 = int(input("Введите r2 = "))

area = area_ring(r1, r2)
print('Area of the ring: ', area)