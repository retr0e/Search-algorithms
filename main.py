import random
import time

# Założenia programu są aby porównać czasy i zoobrazować złożoności obliczeniowe
# 4 wyszukiwań. Do badania wykorzystane będą w listach posortowanych

# -------------Functions-------------


def create_operation_values(values):
    tab = []
    for i in range(0, values):
        tab.append(random.randint(0, 100))
    tab.sort()
    return tab


def linear_search(values):
    s_data = int(input('Jaka wartość chcesz wyszukać?\n'))
    for i in range(0, len(values)):
        if values[i] == s_data:
            return i
    return -1


def binary_search(values, beg, end, search):
    if beg <= end:
        pivot = int((beg + end) / 2)
        if values[pivot] == search:
            return pivot
        elif values[pivot] < search:
            return binary_search(values, pivot + 1, end, search)
        else:
            return binary_search(values, beg, pivot - 1, search)
    return -1


def pattern_search(values, search_pattern):
    result = []
    for i in values:
        if i + len(search_pattern) >= len(values):
            break

        pattern_counter = 0
        if values[i] == search_pattern[0]:
            for j in range(0, len(search_pattern)):
                print(j)
                if values[i + j] == search_pattern[j]:
                    pattern_counter += 1

        if pattern_counter == len(search_pattern):
            result.append(i)

    print(result)
    return result


def create_pattern():
    run_creation = True
    result = []
    while run_creation:
        symbol = input('Podaj liczbe ktora ma zawierac łancuch (znak: x wyłącza stumien wejscia): ')
        if symbol != "x":
            result.append(int(symbol))
        else:
            run_creation = False
    print(result)
    return result

# --------- Implementation Of AVL Tree ---------



# -------------Main program-------------


run_program = True
operation_data = create_operation_values(30)

while run_program:

    print("Twoje dane: ", end='')
    print(operation_data)
    print("1 - Zmien zakres i ilość danych")
    print("2 - Wyszukiwanie liniowe")
    print("3 - Wyszukiwanie binarne")
    print("4 - Wyszukiwanie łańcuchowe")
    print("5 - Wyszukiwanie drzewiaste (AVL)")
    print("6 - Wyjscie")

    decision = int(input("Decyzja: "))

    match decision:
        case 1:
            new_size = int(input("Podaj nowa ilosc: "))
            operation_data = create_operation_values(new_size)
        case 2:
            start_time = time.time()
            result = linear_search(operation_data)
            end_time = time.time()
            if result < 0:
                print('Element nie znajduje sie w zbiorze')
            else:
                print('Element znajduje sie na pozycji: ', result)
                print(operation_data[result])
            print('Czas wyszukiwania wynosil: ', round(end_time - start_time, 2), ' milisekund')
        case 3:
            search_data = int(input('Jaka wartość chcesz wyszukać?'))
            result = binary_search(operation_data, 0, len(operation_data) - 1, search_data)
            print(result)
            print(operation_data[result])
        case 4:
            pattern = create_pattern()
            pattern_search(operation_data, pattern)
        case 5:
            print('That would be funny')
        case 6:
            run_program = False
