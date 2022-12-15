# Напишите программу для. проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

print('Дана таблица истинности: ')
matrix = [
    [0,0,0],
    [0,0,1],
    [0,1,0],
    [0,1,1],
    [1,0,0],
    [1,0,1],
    [1,1,0],
    [1,1,1]
]
print(matrix)
resultLeft = []
resultRight = []
for XYZ in matrix:
    resultLeft.append(not((XYZ[0] or XYZ[1]) or XYZ [2]))
    resultRight.append(not(XYZ[0]) and not(XYZ[1]) and not(XYZ[2]))

print(f"Утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат - {resultLeft==resultRight}")
