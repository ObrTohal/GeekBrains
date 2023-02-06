# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

from math import floor

def binary(n):
    result = []
    while n>1:
        result.append(n%2)
        n = floor(n/2)
    else:
        result.append(n)
        result.reverse()
    strResult = "0b"  
    for i in result:
        strResult+=str(i)
    return strResult

test1 = 45
test2 = 3
test3 = 2
print(f"{binary(test1)} -- {binary(test1)==bin(test1)}")
print(f"{binary(test2)} -- {binary(test2)==bin(test2)}")
print(f"{binary(test3)} -- {binary(test3)==bin(test3)}")