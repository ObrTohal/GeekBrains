# Реализуйте алгоритм перемешивания списка.

import random

def Alg_shuffle(list_of:list):
    for num in range(0,len(list_of)):
        list_of.insert(int(random.random()*len(list_of))%len(list_of),list_of.pop())

lis=[1,2,3,4,5,4,3,2,1,4,5,7,6]
print(lis)
Alg_shuffle(lis)
print(lis)