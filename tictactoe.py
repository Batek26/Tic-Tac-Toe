def print_matrix(input):
    print("---------")
    for i in range(0, len(input), 3):
        print('|', input[i], input[i + 1], input[i + 2], '|')
    print("---------")

def create_matrix(list_of_xo):
    line_1 = []
    line_2 = []
    line_3 = []

    for i in range(9):
        if i < 3:
            line_1.append(list_of_xo[i])
        elif i > 2 and i < 6:
            line_2.append(list_of_xo[i])
        else:
            line_3.append(list_of_xo[i])

    matrix = [line_1, line_2, line_3]

    return matrix

def create_list(matrix):
    input_list = []

    for i in range(9):
        if i < 3:
            input_list.append(matrix[0][i])
        elif i > 2 and i < 6:
            input_list.append(matrix[1][i - 3])
        else:
            input_list.append(matrix[2][i - 6])

    return input_list

def input_symbol(table):
    matrix = create_matrix(table)
    while True:
        try:
            symbol_cord = input()
            x_str, y_str = symbol_cord.split()
            x = int(x_str)
            y = int(y_str)
            while x > 3 or x < 1 or y > 3 or y < 1:
                symbol_cord = input('Coordinates should be from 1 to 3!')
                x_str, y_str = symbol_cord.split()
                x = int(x_str)
                y = int(y_str)
            else:
                while matrix[x - 1][y - 1] != '_':
                    symbol_cord = input('This cell is occupied! Choose another one!')
                    x_str, y_str = symbol_cord.split()
                    x = int(x_str)
                    y = int(y_str)
                else:
                    amount_x = table.count('X')
                    amount_o = table.count('O')
                    if abs(amount_x - amount_o) == 0:
                        matrix[x - 1][y - 1] = 'X'
                    else:
                        matrix[x - 1][y - 1] = 'O'
        except ValueError:
            print('You should enter numbers!')
        else:
            break

    list_of_xo = ''.join(create_list(matrix))
    print_matrix(list_of_xo)
    return list_of_xo

def check_winner(list_1, list_2, list_3):
    x_wins = 0
    o_wins = 0
    for i in range(len(list_1)):
        if list_1[i] == 'XXX':
            x_wins += 1
        elif list_1[i] == 'OOO':
            o_wins += 1
    for i in range(len(list_2)):
        if list_2[i] == 'XXX':
            x_wins += 1
        elif list_2[i] == 'OOO':
            o_wins += 1
    for i in range(len(list_3)):
        if list_3[i] == 'XXX':
            x_wins += 1
        elif list_3[i] == 'OOO':
            o_wins += 1
    return x_wins, o_wins

def analyze_grid(input):
    horizontal = [input[:3], input[3:6], input[6:]]
    vertical = [input[::3], input[1::3], input[2::3]]
    diagonal = [input[::4], input[2:8:2]]
    x_wins = False
    o_wins = False
    draw = False
    if check_winner(horizontal, vertical, diagonal) == (1, 0):
        print('X wins')
        x_wins = True
    elif check_winner(horizontal, vertical, diagonal) == (0, 1):
        print('O wins')
        o_wins = True
    elif check_winner(horizontal, vertical, diagonal) == (0, 0) and input.count('_') == 0:
        print('Draw')
        draw = True

    return any([x_wins, o_wins, draw])



def main():
    tic_tac_toe = ('_________')
    print_matrix(tic_tac_toe)
    while True:
        tic_tac_toe = input_symbol(tic_tac_toe)
        if analyze_grid(tic_tac_toe) is True:
            break



if __name__ == '__main__':
    main()
