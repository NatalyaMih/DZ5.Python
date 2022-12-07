#Создайте программу для игры с конфетами человек против человека.
#Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
#  Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
#  Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?


from random import randint

def input_dat(name):
    x = int(input("{}, введите количество конфет, которое возьмете от 1 до 28: ".format(name)))
    while x < 1 or x > 28:
        x = int(input("{}, введите корректное количество конфет: ".format(name)))
    return x


def p_print(name, k, counter, value):
    print("Ходил {}, он взял {}, теперь у него {}. Осталось на столе {} конфет.".format(name, k, counter, value))

player1 = input("Введите имя первого игрока: ")
player2 = input("Введите имя второго игрока: ")
value = int(input("Введите количество конфет на столе: "))
flag = randint(0,2) # флаг очередности
if flag:
    print("Первый ходит {}".format(player1))
else:
    print("Первый ходит {}".format(player2))

counter1 = 0 
counter2 = 0

while value > 28:
    if flag:
        k = input_dat(player1)
        counter1 += k
        value -= k
        flag = False
        p_print(player1, k, counter1, value)
    else:
        k = input_dat(player2)
        counter2 += k
        value -= k
        flag = True
        p_print(player2, k, counter2, value)

if flag:
    print("Выиграл {}".format(player1))
else:
    print("Выиграл {}".format(player2))



 #Создайте программу для игры в ""Крестики-нолики"". 

"""maps = [1,2,3,
        4,5,6,
        7,8,9]
 
victories = [[0,1,2],
             [3,4,5],
             [6,7,8],
             [0,3,6],
             [1,4,7],
             [2,5,8],
             [0,4,8],
             [2,4,6]]
 
def print_maps():
    print(maps[0], end = " ")
    print(maps[1], end = " ")
    print(maps[2])
 
    print(maps[3], end = " ")
    print(maps[4], end = " ")
    print(maps[5])
 
    print(maps[6], end = " ")
    print(maps[7], end = " ")
    print(maps[8])    
def step_maps(step,symbol):
    ind = maps.index(step)
    maps[ind] = symbol
 
def get_result():
    win = ""
 
    for i in victories:
        if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
            win = "X"
        if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
            win = "O"   
             
    return win
 
game_over = False
player1 = True
 
while game_over == False:
 
    print_maps()
 
    if player1 == True:
        symbol = "X"
        step = int(input("Человек 1, ваш ход: "))
    else:
        symbol = "O"
        step = int(input("Человек 2, ваш ход: "))
 
    step_maps(step,symbol) 
    win = get_result() 
    if win != "":
        game_over = True
    else:
        game_over = False
 
    player1 = not(player1)        
        
print_maps()
print("Победил", win)""" 


#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
exit()
with open('file_encode.txt', 'w') as data:
    data.write('WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW')

with open('file_encode.txt', 'r') as data:
    string = data.readline()

def rle_encode(decoded_string):
    encoded_string = [" "]
    count  = 1
    char = decoded_string[0]
    for i in range(1, len(decoded_string)):
        if decoded_string [i] == char:
            count += 1
        else:
            list[encoded_string + encoded_string] = str(count) + char
            char = decoded_string[i]
            count  = 1
            list[encoded_string + encoded_string] = str(count) + char
    return encoded_string


def rle_decode (encoded_string):
    decoded_string = [" "]
    char_amount = [" "]
    for i in range(len(encoded_string)):
        if encoded_string[i].isdigit():
            char_amount += encoded_string[i]
        else:
            decoded_string += encoded_string[i] * int(char_amount)
        char_amount = [" "]
    print(decoded_string)

    return decoded_string


with open('file_encode.txt', 'r') as file:
    decoded_string = file.read()

with open('file_decode.txt', 'w') as file:
    encoded_string = rle_encode(decoded_string)
    file.write(encoded_string)

print('Decoded string: \t' + decoded_string)
print('Encoded string: \t' + rle_encode(decoded_string))
print('Compress ratio: \t{}'.format (round(len(decoded_string) / len(encoded_string), 1)))