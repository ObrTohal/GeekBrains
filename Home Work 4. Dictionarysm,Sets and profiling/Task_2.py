# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

def factor(number):
    ans = set()
    devider = 2
    while devider*devider <= number:
        if number % devider == 0:
            number/=devider
            ans.add(devider)
        else:
            devider+=1
    if number > 1:
        ans.add(int(number))
    return ans

int_num = int(input('Задайте натуральное число N: '))
print(f'Список простых множителей числа {int_num} = {factor(int_num)}')
