# Task 4.
# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

quarter = int(input("Введите номер четверти: "))
while quarter<1 or quarter>4:
    quarter = int(input("Неверный номер четверти! 1я 2я 3я или 4я четверть.\nВведите номер четверти: "))

if quarter==1:
    print(f"Диапазон возможных координат точек в {quarter} четверти (x и y): \nx в диапазоне - (0,+Inf)\ny в диапазоне - (0,+Inf)")
if quarter==2:
    print(f"Диапазон возможных координат точек в {quarter} четверти (x и y): \nx в диапазоне - (-Inf,0)\ny в диапазоне - (0,+Inf)")
if quarter==3:
    print(f"Диапазон возможных координат точек в {quarter} четверти (x и y): \nx в диапазоне - (-Inf,0)\ny в диапазоне - (-Inf,0)")
if quarter==4:
    print(f"Диапазон возможных координат точек в {quarter} четверти (x и y): \nx в диапазоне - (0,+Inf)\ny в диапазоне - (-Inf,0)")