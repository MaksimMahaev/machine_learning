from random import random
from math import sqrt


#Матрица игры
matrix_game = [[2, -3],
                [-1, 2]]

#Генератор случайных чисел
def _random_(probability):
    r = random()
    if r <= probability:
        d = 0
    else:
        d = 1
    return d


#Симуляция первой или второй игры
def game_one_or_two(probabilityA, probabilityB):
    games = 100 #Количество игр в симуляции
    game_result = 0 #Результат игр
    res_matrix = [] #Вектор из 100 пар бинарных чисел
    for i in range(games):
        game_summary = matrix_game[_random_(probabilityA)][_random_(probabilityB)]
        res_matrix.append(game_summary)
        game_result = game_result+game_summary
    average_winningsA = game_result/games
    print('Вероятность выбора игрока А:', probabilityA)
    print('Вероятность выбора игрока B:', probabilityB)
    print('Выигрыш А:', game_result)
    print('Выигрыш В:', -game_result)
    print('Средний выигрыш А за одну игру:', average_winningsA)
    expected = 8*probabilityA*probabilityB - 5*probabilityA - 3*probabilityB + 2# Мат.ожидание
    print('Математическое ожидание:', expected)
    dev = 0  # СКО
    for x in res_matrix:
        dev += pow(((x - average_winningsA)),2)
    dev = pow((dev / (games - 1)), 0.5)
    print('Среднеквадратичное отклоение:', dev)
    disper = (-2*probabilityA*probabilityB - 3*probabilityB + 5*probabilityA + 4) - pow(expected, 2)# Дисперсия
    print('Дисперсия:', disper)
    print('Теоретическое СКО:', pow(disper,0.5))


#Симуляция третей игры
def game_three(probabilityB):
    games = 100 #Количество игр в симуляции
    game_result = 0 #Результат игр
    res_matrix = [] #Вектор из 100 пар бинарных чисел
    box = [10, 10] #Коробочка для игры с подкреплением
    probabilityA = box[0]/(box[0] + box[1])
    for i in range(games):
        randomiseA = _random_(probabilityA)
        game_summary = matrix_game[randomiseA][_random_(probabilityB)]
        if game_summary > 0:
            box[randomiseA] += 2
        probabilityA = box[0]/(box[0] + box[1])
        res_matrix.append(game_summary)
        game_result += game_summary
    average_winningsA = game_result/games
    print('Обучение игрока А с подкреплением')
    print('Вероятность выбора игрока А к концу игры:', probabilityA)
    print('Вероятность выбора игрока B:', probabilityB)
    print('Выигрыш А:', game_result)
    print('Выигрыш В:', -game_result)
    print('Средний выигрыш А за одну игру:', average_winningsA)
    expected = 8*probabilityA * probabilityB - 5*probabilityA - 3*probabilityB + 2# Мат.ожидание
    print('Математическое ожидание:', expected)
    dev = 0#СКО
    for x in res_matrix:
        dev += pow(((x - average_winningsA)), 2)
    dev = pow((dev / (games - 1)), 0.5)
    print('Среднеквадратичное отклоение:', dev)
    disper = (-2*probabilityA * probabilityB - 3*probabilityB + 5*probabilityA + 4) - pow(expected, 2)# Дисперсия
    print('Дисперсия:', disper)
    print('Теоретическое СКО:', pow(disper, 0.5))


#Симуляция четвертой игры
def game_four(probabilityB):
    games = 100 #Количество игр в симуляции
    game_result = 0 #Результат игр
    res_matrix = [] #Вектор из 100 пар бинарных чисел
    box = [100, 100] #Коробочка для игры с наказанием
    probabilityA = box[0]/(box[0] + box[1])
    for i in range(games):
        randomiseA = _random_(probabilityA)
        game_summary = matrix_game[randomiseA][_random_(probabilityB)]
        if game_summary < 0:
            box[randomiseA] += game_summary
        probabilityA = box[0]/(box[0] + box[1])
        res_matrix.append(game_summary)
        game_result += game_summary
    average_winningsA = game_result/games
    print('Обучение игрока А с наказанием')
    print('Вероятность выбора игрока А к концу игры:', probabilityA)
    print('Вероятность выбора игрока B:', probabilityB)
    print('Выигрыш А:', game_result)
    print('Выигрыш В:', -game_result)
    print('Средний выигрыш А за одну игру:', average_winningsA)
    expected = 8*probabilityA * probabilityB - 5*probabilityA - 3*probabilityB + 2# Мат.ожидание
    print('Математическое ожидание:', expected)
    dev = 0 #СКО
    for x in res_matrix:
        dev += pow(((x - average_winningsA)), 2)
    dev = pow((dev / (games - 1)), 0.5)
    print('Среднеквадратичное отклоение:', dev)
    disper = (-2*probabilityA*probabilityB - 3*probabilityB + 5*probabilityA + 4) - pow(expected, 2)# Дисперсия
    print('Дисперсия:', disper)
    print('Теоретическое СКО:', pow(disper, 0.5))


#Симуляция третей игры
def game_five():
    games = 100 #Количество игр в симуляции
    game_result = 0 #Результат игр
    res_matrix = [] #Вектор из 100 пар бинарных чисел
    boxA = [10, 10] #Коробочка для игры с подкреплением
    boxB = [10,10] #Коробочка для игры с подкреплением
    probabilityA = boxA[0]/(boxA[0] + boxA[1])
    probabilityB = boxB[0]/(boxB[0] + boxB[1])
    for i in range(games):
        randomiseA = _random_(probabilityA)
        randomiseB = _random_(probabilityB)
        game_summary = matrix_game[randomiseA][randomiseB]
        if game_summary > 0:
            boxA[randomiseA] += game_summary
        else:
            boxB[randomiseB] -= game_summary
        probabilityA = boxA[0]/(boxA[0] + boxA[1])
        probabilityB = boxB[0] / (boxB[0] + boxB[1])
        res_matrix.append(game_summary)
        game_result += game_summary
    average_winningsA = game_result/games
    print('Обучение игрока А с подкреплением и игока В с подкреплением')
    print('Вероятность выбора игрока А к концу игры:', probabilityA)
    print('Вероятность выбора игрока B к концу игры:', probabilityB)
    print('Выигрыш А:', game_result)
    print('Выигрыш В:', -game_result)
    print('Средний выигрыш А за одну игру:', average_winningsA)
    expected = 8*probabilityA * probabilityB - 5 *probabilityA - 3*probabilityB + 2 # Мат.ожидание
    print('Математическое ожидание:', expected)
    dev = 0 #СКО
    for x in res_matrix:
        dev += pow(((x - average_winningsA)), 2)
    dev = pow((dev / (games - 1)), 0.5)
    print('Среднеквадратичное отклоение:', dev)
    disper = (-2*probabilityA*probabilityB - 3*probabilityB + 5*probabilityA + 4) - pow(expected, 2) # Дисперсия
    print('Дисперсия:', disper)
    print('Теоретическое СКО:', pow(disper, 0.5))

#print(game_one_or_two(0.5,0.5))
#print(game_one_or_two(0.5,0.25))
#print(game_three(0.25))
#print(game_four(0.25))
#print(game_five())






