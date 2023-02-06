# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def pos_fibo(N):
    resFibo = [0,1]
    for i in range(1,N):
        resFibo.append(resFibo[i]+resFibo[i-1])
    return resFibo

def nego_fibo(N):
    resFibo = [1,-1]
    for i in range(0,N-2):
        resFibo.append(resFibo[i]-resFibo[i+1])
    resFibo.reverse()
    return resFibo

k = 8
fibonachi = nego_fibo(k)
fibonachi += pos_fibo(k)
print(fibonachi)