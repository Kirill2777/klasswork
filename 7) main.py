#coding: utf-8
#Задача 7 
def min_of_two(a, b):
 if a < b:
  return a
 else:
  return b

a = float(input("Введите  a  = "))
b = float(input("Введите  b = "))

print('Меньшее число:', min_of_two(a, b))