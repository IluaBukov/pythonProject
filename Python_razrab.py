
field  = [1,2,3,4,5,6,7,8,9]

wins = [(1,2,3),(4,5,6),(7,8,9),
        (1,4,7),(2,5,8),(3,6,9),
        (1,5,9),(3,5,7)]

def x_o_field():
    for i in range(3):
        print(field[0 + i * 3],field[1 + i * 3],field[2 + i * 3])
def light_i(lig):
    while True:
        where = input("куда поставим символ? " + lig +":")
        if not (where in " 123456789 "
                         ""):
            print("ошибка ввода")
            continue

        where = int(where)
        if str(field[where - 1])in "XO":
            print("клетка занята!!!")
            continue
        field[where - 1] = lig
        break

def wins_test():
    for a in wins:
        if (field[a[0]-1]) == (field[a[1]-1]) == (field[a[2]-1]):
            return field[a[1]-1]
    else:
        return False
def spl():
    last = 0
    while True:
        x_o_field()
        if last % 2 == 0:
            light_i("X")
        else:
            light_i("O")
            if last > 3:
                winner = wins_test()
                if winner:
                    x_o_field()
                    print(winner, "выйграл")
                    break
        last += 1
        if last > 8:
            x_o_field()
            print("победила дружба !")
            break
spl()
