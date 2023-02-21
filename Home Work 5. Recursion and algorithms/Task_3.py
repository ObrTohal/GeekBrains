# Создайте программу для игры в ""Крестики-нолики"".
import os
def begin_game():
    os.system('clear')
    print("""Добро пожаловать в игру 'Крестики-нолики'!!!

             Главное меню:
                (введите пункт меню)
             1 - Начать игру
             0 - Выход
          """)
    choise = int(input())
    while choise > 3 or choise <= 0:
        choise = int(input("Неккоректный пункт меню, введите пункт меню 1,2 или 3:"))

    if choise==1:
        load_pvp_game()
    elif choise==0:
        exit()

def load_pvp_game():
    os.system('clear')
    battleground_massive = [[' ', ' ', ' '],
                            [' ', ' ', ' '],
                            [' ', ' ', ' ']]
    players_moves = {'X':[[' ', ' ', ' '],
                          [' ', ' ', ' '],
                          [' ', ' ', ' ']],
                     'O':[[' ', ' ', ' '],
                          [' ', ' ', ' '],
                          [' ', ' ', ' ']]}
    print("""
    Первые ходят Х, затем О
    Укажите координаты через пробел где хотите поставить символ
    Пример:
    1 1 
    ~~~~~~~~~~~~~~~~~~~~~~~~~~
     1   2    3
  1  Х |   |
    ---|---|---
  2    |   |
    ---|---|---
  3    |   |
    
    Первый ход за Х ->:
    """)

    x,y = player_move('X',players_moves)
    last_move_player = 'X'
    clear_battleground()
    battleground_massive[int(x)-1][int(y)-1] = 'X'
    update_battleground(battleground_massive)
    player, win = check_win(players_moves)
    while not win:
        if last_move_player == "X":
            print("Ход О ->")
            last_move_player = 'O'
            x,y = player_move('O',players_moves)
            clear_battleground()
            battleground_massive[int(x)-1][int(y)-1] = 'O'
        else:
            print("Ход X ->")
            last_move_player = 'X'
            x,y = player_move('X',players_moves)
            clear_battleground()
            battleground_massive[int(x)-1][int(y)-1] = 'X'
        player, win = check_win(players_moves)
        update_battleground(battleground_massive)
    else:
        print(f"Победили: {player}")

def player_move(player,players_moves):
    x,y = input().split(" ")
    if 0 < int(x) < 4 and 0 < int(y) < 4:
        if (players_moves['X'][int(x)-1][int(y)-1] == ' ') and\
            (players_moves['O'][int(x)-1][int(y)-1] == ' '):
            if player == "X":
                players_moves['X'][int(x)-1][int(y)-1]='X'
            elif player == "O":
                players_moves['O'][int(x)-1][int(y)-1]='O'
            return (x,y)
        else:
           print("Эта ячейка уже занята! Введите другую ячейку!") 
           return player_move(player,players_moves)
    else:
        print("Введите значение в диапазоне от 1 до 3 !!")
        return player_move(player,players_moves)

def check_win(moves:dict):
    for player in moves:        #Проход по сделанным ходам
        count_d = 0
        count_rd =0
        count_row = 0
        count_col = 0
        rows = [row for row in moves[player]]
        columns = []
        diag = []
        r_diag = []
        for r in range(len(rows)):  #разделение на выигрышные комбинации
            elems =[]
            for c in range(len(rows)):
                elems.append(rows[c][r])
                if c==r:
                    diag.append(rows[c][r])
                    r_diag.append(rows[-c-1][r])
            columns.append(elems)
        for _set_ in rows:
            count_row = _set_.count(player)
            if count_row == 3:
                return (player,True)
        for _set_ in columns:
            count_col = _set_.count(player)
            if count_col == 3:
                return (player,True)
        count_d = diag.count(player)
        count_rd = r_diag.count(player)
        if(count_col and count_row):    #если ход был сделан
            if  (count_d%3==0 and player in diag) or\
                (count_rd%3==0 and player in r_diag):
                return (player,True)
    return (' ',False)

def update_battleground(battleground_massive):
    os.system('clear')
    print('''
     1   2   3''')
    check_last =1
    for strok in battleground_massive:
        print(f"  {check_last} ",end=' ')
        print(*strok,sep=" | ")
        print("   ",end=' ')
        if check_last != 3:
            print("---|---|---")
            check_last+=1
    

def clear_battleground():
    os.system('clear')
    battleground= '''
     1   2   3
  1    |   |
    ---|---|---
  2    |   |
    ---|---|---
  3    |   |
    '''
    print(battleground)

begin_game()