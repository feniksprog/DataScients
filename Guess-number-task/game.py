"""Игра угадай число"""

import numpy as np

number = np.random.randint(1, 101) # загадываем число


count = 0 # количество попыток
start = 1 # число с которого начинать поиск
end = 101 # число которым заканчивать поиск
predict_number = int((end-1)/2) # начинаем поиск с середины

def psevdo_random(i = 1, j = 101):
    predict_number_random = np.random.randint(i, j)  # предполагаемое число
    return predict_number_random


while True:
    count+=1
    
    if predict_number > number:
        print(f"Число должно быть меньше чем {predict_number}!")
        start = start
        end = predict_number

    elif predict_number < number:
        print(f"Число должно быть больше чем {predict_number}!")
        start = predict_number+1
        end = end
    
    else:
        print(f"Вы угадали число! Это число = {number}, за {count} попыток")
        break #конец игры выход из цикла
    
    predict_number = psevdo_random(start, end)  # предполагаемое число    
