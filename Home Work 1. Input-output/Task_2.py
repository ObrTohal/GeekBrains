# Task 2.
# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# для всех значений предикат.
             #X #Y #Z
predicats = [[0, 0, 0],
             [0, 0, 1],
             [0, 1, 0],
             [0, 1, 1],
             [1, 0, 0],
             [1, 0, 1],
             [1, 1, 0],
             [1, 1, 1]]

def checkBool(predicat):
    for set_p in predicat:
        if(not (not (set_p[0] or set_p[1] or set_p[2]) ==
           (not set_p[0] and not set_p[1] and not set_p[2]))):
            return
    print("Утверждение истино")

checkBool(predicats)