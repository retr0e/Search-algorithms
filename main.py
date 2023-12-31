import random
import time

# Założenia programu są aby porównać czasy i zoobrazować złożoności obliczeniowe
# 4 wyszukiwań. Do badania wykorzystane będą w listach posortowanych

# -------------Functions-------------


def create_operation_values(values):
    tab = []
    for i in range(0, values):
        tab.append(random.randint(0, 100000))
    tab.sort()
    return tab

# --------- Linear search ---------


def linear_search(values):
    s_data = int(input('Jaka wartość chcesz wyszukać?\n'))
    for i in range(0, len(values)):
        if values[i] == s_data:
            return i
    return -1

# --------- Binary search ---------


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

# --------- Jump search ---------


def jump_search(values, searched_value):
    jump = 4
    jump_control = 0

    backwards = False

    while jump_control + jump < len(values):

        if values[jump_control] == searched_value:
            return jump_control

        if values[jump_control] > searched_value:
            backwards = True
            break

        jump_control += jump

    if backwards:
        for i in range(jump_control, 0, -1):
            if values[i] == searched_value:
                return i
    else:
        for i in range(0, len(values)):
            if values[i] == searched_value:
                return i

# --------- Implementation Of AVL Tree ---------


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:

    def insert(self, root, value):
        if not root:
            return Node(value)
        elif value < root.value:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        # Rotacje
        if balance > 1:
            if value < root.left.value:
                return self.right_rotate(root)
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)

        if balance < -1:
            if value > root.right.value:
                return self.left_rotate(root)
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)

        return root

    def left_rotate(self, z):
        if z is None or z.right is None:
            return z

        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def right_rotate(self, y):
        if y is None or y.left is None:
            return y

        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return x

    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def search(self, root, value):
        if not root or root.value == value:
            return root

        if value < root.value:
            return self.search(root.left, value)
        return self.search(root.right, value)

# -------------Main program-------------


run_program = True
operation_data = create_operation_values(30)

while run_program:

    print("Twoje dane: ", end='')
    print(operation_data)
    print("1 - Zmien zakres i ilość danych")
    print("2 - Wyszukiwanie liniowe")
    print("3 - Wyszukiwanie binarne")
    print("4 - Wyszukiwanie skokowe")
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
            print('Czas wyszukiwania liniowego wynosil: ', end_time - start_time, ' milisekund')
        case 3:
            search_data = int(input('Jaka wartość chcesz wyszukać?\n'))
            start_time = time.time()
            result = binary_search(operation_data, 0, len(operation_data) - 1, search_data)
            end_time = time.time()
            print(result)
            print(operation_data[result])
            print('Czas wyszukiwania binarnego wynosil: ', end_time - start_time, ' milisekund')
        case 4:
            search_data = int(input('Jaka wartość chcesz wyszukać?\n'))
            start_time = time.time()
            result = jump_search(operation_data, search_data)
            end_time = time.time()
            if not result:
                print('Nie znaleziono takiego elementu w zbiorze!')
            else:
                print(result)
            print('Czas wyszukiwania skokowego wynosil: ', end_time - start_time, ' milisekund')
        case 5:
            avl_tree = AVLTree()
            root = None
            for element in operation_data:
                root = avl_tree.insert(root, element)
            search_data = int(input('Jaka wartość chcesz wyszukać?\n'))
            start_time = time.time()
            result = avl_tree.search(root, search_data)
            end_time = time.time()
            if not result:
                print('Nie znaleziono takiego elementu w zbiorze!')
            else:
                print(result.value)
            print('Czas wyszukiwania elementu za pomocą drzewa AVL wynosil: ', end_time - start_time,
                  ' milisekund')
        case 6:
            print('Bye Bye!')
            run_program = False
