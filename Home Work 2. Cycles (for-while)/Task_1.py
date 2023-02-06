# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# 
# Пример:
#
# - 6782 -> 23
# - 0,56 -> 11

inputNum = input("Введите число: ")
# Решение 1: в одну строчку:
print(sum(map(lambda num: int(num),list(filter(lambda num: (num.isdigit()), list(inputNum))))))

# Решение 2:
sum=0
strInputNumber = list(inputNum)
for element in strInputNumber:
    if str(element).isdigit():
        sum+=int(element)
print(f"{inputNum} -> {sum}")