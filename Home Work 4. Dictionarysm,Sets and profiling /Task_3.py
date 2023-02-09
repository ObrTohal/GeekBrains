# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

#Решение без использования set
def unique_elements(numbers):
    checking = [False]*(max(numbers)+1)
    ans =[]
    for element in numbers:
        if(not checking[element]):
            checking[element] = True
            ans.append(element)
    return ans

#Решение с использование set
def unique_elements_set(numbers):
    return set(numbers)
    
#Проверка    
numbers = [1,1,1,1,2,2,2,3,3,3,4]
print(f"{numbers} - > {unique_elements(numbers)}")
print(f"{numbers} - > {unique_elements_set(numbers)}")