body = [[" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]]
print("Добро пожаловать в игру Крестики-Нолики!")

def show_body():
    print(" ")
    print('       0   1   2')
    print("      ------------")
    for i in range(3):
        row = " | ".join(body[i])
        print([f'{i}  | {row} | '])
    print("      ------------")


def question_of_cords():
    while True:
        cords = input("Вы походите: ").split()
        if len(cords) != 2:
            print("Пишите две координаты!")
            continue

        x, y = cords

        if not(x.isdigit()) and not(y.isdigit()):
            print("Пишите координаты цифрами!")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print('Координаты следует писать в значении от 0 до 2!')
            continue

        if body[x][y] != " ":
            print("Клетка занята!")
            continue
        return x, y


def win():
    cord_for_win = [((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                    ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)),
                    ((0, 0), (1, 1), (2, 2)), ((0, 2), (1, 1), (2, 0))]

    for cord in cord_for_win:
        symbol = []
        for c in cord:
            symbol.append(body[c[0]][c[1]])
        if symbol == ['X', 'X', 'X']:
            print("Выиграл игрок с крестиком!")
            return True
        if symbol == ['O', 'O', 'O']:
            print("Выиграл игрок с ноликом!")
            return True
    return False


count = 0
while True:
    count += 1

    show_body()

    if count % 2 == 1:
        print("Ходит игрок с крестиком")
    else:
        print("Ходит игрок с ноликом")

    x, y = question_of_cords()

    if count % 2 == 1:
        body[x][y] = "X"
    else:
        body[x][y] = "O"

    if win():
        break

    if count == 9:
        print("Ничья")
        break
