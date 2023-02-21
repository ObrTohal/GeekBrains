#  Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# input_str = input("Введите текст: ")
test_str = "qwef прое ыук абвва вбаыф куе пвабвфф !абв бфывабвю, аа!б!в!ы"

def remove_in_str(input_str:str,removed_str:str) -> str:
    words = input_str.split(" ")
    if input_str != '':
        word = words.pop(0)
        new_str = ' '.join(words)
        if removed_str not in word:
            word+=" "+remove_in_str(new_str,removed_str)
            return word
        else:
            word=remove_in_str(new_str,removed_str)
            return word
    else:
        return ''

print(remove_in_str(test_str,"абв"))