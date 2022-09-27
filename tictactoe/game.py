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

    is_game_end = check_is_game_end(state)

    while not is_game_end:
        print(f'Текущий ход: {current_sign}')

        print_state(state)

        row_number = get_user_input('Строка: ')
        column_number = get_user_input('Ряд: ')

        if state[row_number][column_number] != sign_empty:
            print('Поле уже занято. Выберите другое.')
            continue

        state[row_number][column_number] = current_sign

        current_sign = get_current_sign(current_sign)
