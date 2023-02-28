# Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
import random as R
import os
os.system('clear')

mass_list = [R.randint(0,10) for _ in range(11)]
print("Исходный массив: {}".format(mass_list))
min,max = input('Введите диапазон через пробел: ').split(' ')
indexes = [index for index in range(len(mass_list)) if mass_list[index]>=int(min) and mass_list[index]<=int(max)]

print("Индексы элементов массива, значения которых принадлежат диапазону [{},{}]: \n{}".format(min,max,indexes))