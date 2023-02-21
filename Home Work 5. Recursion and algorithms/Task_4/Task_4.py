"""
5 - Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.
файл первый:
AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool
файл второй:
сжатый текст.
"""

def encode(file):
    encoding = ""
    with open(file,'r') as file_in:
        s=file_in.read()
        i = 0
        while i < len(s):
            count = 1
            while i + 1 < len(s) and s[i] == s[i + 1]:
                count = count + 1
                i = i + 1
            encoding += str(count) + s[i]
            i = i + 1
    with open(file+".RLE",'w') as file_out:
        file_out.write(encoding)
    print("File encoded!!!")

def decode(file):
    decoding = ""
    with open(file,'r') as file_in:
        s=file_in.read()
        num=""
        i = 0
        while i < len(s):
            if(s[i].isdigit()):
                num+=s[i]
            else:
                count =0
                for count in range(int(num)):
                    decoding+=s[i]
                num=""
            i+=1

    with open(str(file).replace(".RLE",".decod"),'w') as file_out:
        file_out.write(decoding)
    print("File decoded!!!")

encode('Home Work 5. Recursion and algorithms/Task_4/test')
decode('Home Work 5. Recursion and algorithms/Task_4/test.RLE')
