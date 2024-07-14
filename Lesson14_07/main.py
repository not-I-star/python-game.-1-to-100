# import game

# game.sum(5, 2, 2)

# game.play(4, 2)


# from game import play 

# play(2, 5)


import random 

# Минимальное и максимальное число для игры
min_number = 1
max_number = 100

# кол-во ходов до поражения
number_to_lose = 5

# ход бота
botChoice = random.randint(min_number, max_number)

# объявление по игре 
print(f'Я загадал число от {min_number} до {max_number}. У тебя {number_to_lose} попыток угадать.')

while True:  
    # подсчет попыток 
    number_to_lose -= 1
# проверка на конец игры
    if number_to_lose == -1:
        print(f'Вы проигали! Число было: {botChoice}!')
        break 
    # ход игрока 
    userChoice = int(input('Ваш ход, впишите число: '))

    # ход игры 

    if userChoice == botChoice:
        print('Вы угадали!')
        break
    # проверка на правильность числа в рамках мин и макс
    elif userChoice < min_number or userChoice > max_number:
        print(f'Некорректный ввод! Введите число от {min_number} до {max_number}!')
    elif userChoice < botChoice:
        print(f'Выберите число больше! Осталось попыток: {number_to_lose}.')
    elif userChoice > botChoice:
        print(f'Выберите число меньше! Осталось попыток: {number_to_lose}.')
    

    
   




# myList = [1, 4, 5, 2, 7, 8, 9]
# print(random.choice(myList))