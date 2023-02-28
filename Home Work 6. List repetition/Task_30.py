# Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
import os
os.system('clear')

def input_first_diff_size():
    first=0
    diff=0
    size=0
    while True:
        try:
            first = int(input('Введите первый элемент арифметической прогрессии: '))
            diff = int(input('Введите разность арифметической прогрессии: '))
            size = int(input('Введите размер массива элементов арифметической прогрессии: '))
            if size <= 0: 
                print("Кол-во элементов не может быть отрицательным или равным нулю!")
                continue
            break
        except ValueError as ValEr:
            print(ValEr)
            print("Нужно ввести целое число!!!")
    return (first,diff,size)

def create_list(a1:int,d:int,n:int):
    result_list = [a1+(n-1)*d for n in range(1,n+1)]
    return result_list

first,diff,size = input_first_diff_size()
mass = create_list(first,diff,size)
print('Массив заполненный элементами арифметической прогрессии: {}'.format(mass))