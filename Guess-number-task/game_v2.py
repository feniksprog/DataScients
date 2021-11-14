"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np

def psevdo_random(i: int = 1, j: int = 101)-> int:
    """Рандомно генерирует число в заданном диапазоне

    Args:
        i (int, optional): Минимальное число из диапазона рандома. Defaults to 1.
        j (int, optional): Максимальное число из диапазона рандома. Defaults to 101.

    Returns:
        int: Рандомное число
    """
    np.random.seed()  # генерируемая последовательность для рандома каждый раз разная   
    predict_number_rundom = np.random.randint(i, j)  # предполагаемое число     
    return predict_number_rundom

def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0 # количество попыток
    start = 1 # число с которого начинать поиск
    end = 101 # число которым заканчивать поиск
    
    predict_number = int((end-1)/2) # начинаем поиск с середины
            
    while True:
        count+=1

        if predict_number > number:
            #print(f"Число должно быть меньше чем {predict_number}!")
            start = start
            end = predict_number

        elif predict_number < number:
            #print(f"Число должно быть больше чем {predict_number}!")
            start = predict_number+1
            end = end
        
        else:
            #print(f"Вы угадали число! Это число = {number}, за {count} попыток")
            break #конец игры выход из цикла
        
        predict_number = psevdo_random(start, end)  # предполагаемое число  
        
        #if count >= 20:
            #print(f"ПРОВАЛ!!!!!!! Это число = {number}, за {count} попыток")
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
