#coding: utf-8
#Задача 5
def bigger(a, b):
	if a > b:
		return a
	else:
		return b

a = int(input("Введите a = "))
b = int(input("Введите b = "))

result = bigger(a, b)
print(result)