# Вычислить число c заданной точностью d

# Пример:

# при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
from decimal import Decimal
def calculation_pi_with_precision(d):
    '''
        Вычисление PI по ряду Никаланта
    '''
    pi_cure = 3
    pi_prev = 0
    cycle =1
    delim_ind_start = 2
    str_d = str(d)
    # Если есть убираем научную нотацию
    if 'e' in str_d:
        str_d = ''.join(['0' for _ in range(int(str_d[str_d.find('e-')+2]), int(str_d[str_d.find('e-')+2].join(str_d[str_d.find('e-')+2:]))-1) ])
        str_d = '0.{}1'.format(str_d)
    # Запоминаем кол-во знаков после запятой (для выдачи результата)
    ndigits = abs(str_d.find('.')-len(str_d))-1
    # Основной цикл
    while abs(pi_cure-pi_prev)>d:
        pi_prev = pi_cure
        # Расчет произведений делителя
        delim =1
        for num in range(delim_ind_start,delim_ind_start+3):
            delim *= num
        # Выбор знака
        if cycle%2 == 0: 
            pi_cure-=4/delim
        else:
            pi_cure+=4/delim
        # Инкремент
        cycle+=1
        delim_ind_start+=2
    return round(pi_cure,ndigits)

for d in range(-1,-10,-1):
    print(f'При d = {10**(d)} -> PI = {calculation_pi_with_precision(10**(d))}')