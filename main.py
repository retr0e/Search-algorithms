import random

# -------------Functions-------------


def create_operation_values(values):
    tab = []
    for i in range(0, values):
        tab.append(random.randint(0, values))
    tab.sort()
    return tab


def linear_search(values):
    search_data = int(input('Jaka wartość chcesz wyszukać?'))
    for i in range(0, len(values)):
        if values[i] == search_data:
            return i
    return -1


# def binary_search(values, search_data):


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
operation_data = create_operation_values(20)

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
            result = linear_search(operation_data)
            if result < 0:
                print('Element nie znajduje sie w zbiorze')
            else:
                print('Element znajduje sie na pozycji: ', result)
                print(operation_data[result])
        case 4:
            pattern = create_pattern()
            pattern_search(operation_data, pattern)
        case 5:
            print()
        case 6:
            run_program = False
