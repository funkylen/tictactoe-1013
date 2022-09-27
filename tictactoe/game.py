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


def start():
    sign_empty = '-'

    state = [
        [sign_empty, sign_empty, sign_empty],
        [sign_empty, sign_empty, sign_empty],
        [sign_empty, sign_empty, sign_empty]
    ]

    print_state(state)

    current_sign = get_current_sign(SIGN_O)
    steps = 9

    while steps > 0:
        print(f'Текущий ход: {current_sign}')

        row_number = int(input('Строка: ')) - 1
        column_number = int(input('Ряд: ')) - 1

        state[row_number][column_number] = current_sign

        print_state(state)

        current_sign = get_current_sign(current_sign)
