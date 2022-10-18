import prompt

SIGN_X = 'X'
SIGN_O = 'O'


def print_state(state):
    field = ''

    for line in state:
        for sign in line:
            field += sign + ' '
        field += "\n"

    print(field)


def get_current_sign(old_sign):
    if old_sign == SIGN_X:
        return SIGN_O

    return SIGN_X


def get_user_input(message):
    min_index = 0
    max_index = 2

    while True:
        number = prompt.integer(message) - 1

        if min_index <= number <= max_index:
            return number


def check_is_game_end(state):
    return False


def start():
    sign_empty = '-'

    state = [
        [sign_empty, sign_empty, sign_empty],
        [sign_empty, sign_empty, sign_empty],
        [sign_empty, sign_empty, sign_empty]
    ]
    

    current_sign = get_current_sign(SIGN_O)

    max_turns = 9

    while max_turns != 0:
        print(f'Текущий ход: {current_sign}')

         
        print_state(state)
        
        if check_win(state) == True:
        
            return
         

        row_number = get_user_input('Строка: ')
        column_number = get_user_input('Ряд: ')

        if state[row_number][column_number] != sign_empty:
            print('Поле уже занято. Выберите другое.')
            continue
        

        state[row_number][column_number] = current_sign

        current_sign = get_current_sign(current_sign)
        max_turns -= 1
    print('Ничья')
    return 
def check_win(state):
    print(state)
    if (state[0][0] == state [0][1] == state[0][2]) and state[0][2] != '-':
        print ('Победил игрок ' + str(state[0][0]))
        return True
    if (state[0][0] == state [1][0] == state[2][0]) and state[2][0] != '-':
        print ('Победил игрок ' + str(state[0][0]))
        return True
    if (state[1][0] == state [1][1] == state[1][2]) and state[1][2] != '-':
        print ('Победил игрок ' + str(state[1][0]))
        return True
    if (state[2][0] == state [2][1] == state[2][2]) and state[2][2] != '-':
        print ('Победил игрок ' + str(state[2][0]))
        return True
    if (state[0][1] == state [1][1] == state[2][1]) and state[0][1] != '-':
        print ('Победил игрок ' + str(state[0][1]))
        return True
    if (state[0][2] == state [1][2] == state[2][2]) and state[0][2] != '-':
        print ('Победил игрок ' + str(state[0][2]))
        return True
    if (state[0][0] == state [1][1] == state[2][2]) and state[0][0] != '-':
        print ('Победил игрок ' + str(state[0][2]))
        return True
    if (state[0][2] == state [1][1] == state[2][0]) and state[0][2] != '-':
        print ('Победил игрок ' + str(state[0][2]))
        return True
    else:
        return False

start()