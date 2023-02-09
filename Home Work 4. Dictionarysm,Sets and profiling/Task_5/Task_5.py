# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

import sys
sys.path.append('Home Work 4. Dictionarysm,Sets and profiling/Task_4')
from Task_4 import gen_polynomial

import re

with open('Home Work 4. Dictionarysm,Sets and profiling/Task_5/Polynom_1.txt','w') as file:
    poly = gen_polynomial(int(input('Введите степень полинома: ')))
    file.write(poly)
    print("Могочлен записан в файл!")

with open('Home Work 4. Dictionarysm,Sets and profiling/Task_5/Polynom_2.txt','w') as file:
    poly = gen_polynomial(int(input('Введите степень полинома: ')))
    file.write(poly)
    print("Могочлен записан в файл!")

def calculate_polynom():
    with open('Home Work 4. Dictionarysm,Sets and profiling/Task_5/Polynom_1.txt','r') as file:
        polynom_1 = file.read()
    with open('Home Work 4. Dictionarysm,Sets and profiling/Task_5/Polynom_2.txt','r') as file:
        polynom_2 = file.read()
    coef_1 = capture_coeff(polynom_1)
    coef_2 = capture_coeff(polynom_2)
    coef_result = {}
    polynom_result = ''
    max_size_of_polynoms = max(len(coef_1.keys()), len(coef_2.keys()))
    for step_1 in range(-1,max_size_of_polynoms):
        if step_1 in coef_1.keys() and step_1 in coef_2.keys():
            coef_result[step_1] = coef_1.pop(step_1) + coef_2.pop(step_1)
        elif step_1 in coef_1.keys():
            coef_result[step_1] = coef_1.pop(step_1)
        elif step_1 in coef_2.keys():
            coef_result[step_1] = coef_2.pop(step_1)

    for step in range(len(coef_result.keys())-2,-2,-1):
        if step in coef_result.keys():    
            if step >1:
                polynom_result += str(coef_result[step])+f'*x^{step} + '
            elif step == 1:
                polynom_result += str(coef_result[step])+f'*x '
            elif step == 0:
                polynom_result += f'+ {coef_result[step]} '
            else:
                polynom_result += f'= {coef_result[step]}'
    return polynom_result

def capture_coeff(polynom: str):
    coeff={}
    step=1 
    for matches in re.finditer(r'(\d+)\*?(x?)(\^(\d+))?',polynom):
        if(matches[4]==None and matches[2]!=None):    
            coeff[step] = int(matches[1])
            step-=1
        else:
            coeff[int(matches[4])] = int(matches[1])
    return coeff

print(calculate_polynom())