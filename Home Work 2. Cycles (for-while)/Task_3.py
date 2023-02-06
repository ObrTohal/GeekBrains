# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$
# и выведите на экран их сумму.
#
# Пример:
#
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

#Результат Для n = 6: {1: 2, 2: 4, 3: 7, 4: 9, 5: 12, 6: 14}

N = int(input("Введите N: "))

def f(N):
    sum = 0
    result ={}
    for num in range(1,N+1):
        sum+=(1+1/num)**num
        result[num] = round(sum)
    return result

print(f(N))