# Задача 1.
# Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.

def checkWeekend(day_in):
    day = day_in #int(input("Введите цифру дня недели: "))
    if(day > 0):
        if(day >= 6 and day <=7):
            print(f'{day} -> да - выходной день')
            return;
        elif(day < 7):
            print(f'{day} -> нет - рабочий день')
            return;
    print(f'Не корректно введена цифра дня недели [{day}]!')

checkWeekend(-1)
checkWeekend(0)
checkWeekend(1)
checkWeekend(2)
checkWeekend(3)
checkWeekend(4)
checkWeekend(5)
checkWeekend(6)
checkWeekend(7)
checkWeekend(8)
checkWeekend(9)
