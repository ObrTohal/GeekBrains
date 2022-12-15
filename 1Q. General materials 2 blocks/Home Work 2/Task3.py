# Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.

# Пример:

# - Для n = 6: [2.0, 2.25, 2.37, 2.44, 2.48, 2.52]

N = int(input("Введите N: "))

def f(N):
    result =[]
    for num in range(1,N+1):
        result.append(round((1+1/num)**num,2)) 
    
    print(result)
    return round(sum(result),2)

print(f(N))