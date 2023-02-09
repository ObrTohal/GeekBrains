# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.

# Пример:

# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random as R

def gen_polynomial(k):
    # старшая степень есть всегда поэтому randint(1,100)
    polynomial=list()
    if(k>1):
        rand_coef = R.randint(1,100)
        if rand_coef>1:
            polynomial = [str(rand_coef)+'x^{}'.format(k)]
        else:
            polynomial = ['x^{}'.format(k)]
    elif k==1:
        rand_coef = R.randint(1,100)
        coef = R.randint(0,100)
        polynomial = [str(rand_coef)+'x']
        if coef !=0:
            polynomial.append(str(coef))
        return (' + '.join(polynomial))+' = 0'
    else:
        return '0'+' = 0'
    k-=1
    # проверка младших стпеней
    while k > 1 :
        rand_coef = R.randint(0,100)
        if rand_coef !=0:
            polynomial.append(str(rand_coef)+'x^{}'.format(k))
        k-=1
    else:
        rand_coef = R.randint(0,100)
        coef = R.randint(0,100)
        if rand_coef !=0:
            polynomial.append(str(rand_coef)+'x')
        if coef !=0:
            polynomial.append(str(coef))
    return (' + '.join(polynomial))+' = 0'

with open('Home Work 4. Dictionarysm,Sets and profiling/Task_4/Task_4_polynom.txt','w') as file:
    file.write(gen_polynomial(int(input('Введите степень полинома: '))))
print("Могочлен записан в файл!")