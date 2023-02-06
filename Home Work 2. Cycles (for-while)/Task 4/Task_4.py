# Задайте список из N элементов, 
# заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

size=int(input("Введите N: "))
numbers = [number for number in range(-size,size+1)]
with open('Home Work 2. Cycles (for-while)/Task 4/file.txt','r') as fd:
    index = [int(ind) for ind in fd.readlines()]
    result =1
    for it in index:
        if(int(it) < len(numbers)): 
            result*=numbers[int(it)]
        else: 
            print('index вне допустиммом пределе... пропуск')
print('Произведение на позициях {} массива {} = {}'.format(index,numbers,result))