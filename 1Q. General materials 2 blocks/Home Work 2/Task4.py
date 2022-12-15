# Задайте спсок из N элементов, заполненных числами из промежутка [-N,N].
# Найдите произведение элементов на указанных позициях. 
# Позиции вводятся с клавиатуры.

N = int(input("Введите N: "))
massive = [num for num in range(-N,N+1)]
print(f"Сформирован массив в пределах [-{N},{N}]: {massive}")

first,second = input("Введите позиции элементов которые нужно перемножить (отсчет от 0) через пробел: ").split(' ')
first_int = int(first)
second_int = int(second)
print(f"Произведение элементов списка на позициях {first_int} ({massive[first_int]}) и {second_int} ({massive[second_int]}) = {massive[first_int]*massive[second_int]}")