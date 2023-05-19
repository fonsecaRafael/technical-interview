WHITE = 'W'
BLACK = 'B'
EMPTY = 'E'


def has_move(board: list, line, column):
    lines = len(board)
    if lines == 0:
        raise Exception('The board must have at least one line')

    columns = len(board[0])
    if columns == 0:
        raise Exception('The board must have at least one column')

    color = board[line][column]
    if color == EMPTY:
        raise Exception("The Initial position, can't be empty")

    def adjacents(position: tuple):
        def interval(value, max_value):
            return range(max(value-1, 0), min(value+2, max_value))

        p_line, p_column = position
        line_interval = interval(p_line, lines)
        column_interval = interval(p_column, columns)

        return [(l, c) for l in line_interval for c in column_interval]

    def has_empty_adjacents(position):
        return any(
            board[p_line][p_column] == EMPTY
            for p_line, p_column in adjacents(position)
        )

    def adjacents_with_same_color(position):
        return [(l, c) for l, c in adjacents(position) if color == board[l][c]]

    to_visit = set([(line, column)])
    visited = set()

    while to_visit:
        current_position = to_visit.pop()
        if has_empty_adjacents(current_position):
            return True
        visited.add(current_position)
        for p in adjacents_with_same_color(current_position):
            if p not in visited:
                to_visit.add(p)

    return False


b_w_u = [
    [EMPTY, WHITE, BLACK, EMPTY],
    [EMPTY, WHITE, BLACK, EMPTY],
    [EMPTY, WHITE, BLACK, EMPTY],
    [EMPTY, WHITE, BLACK, EMPTY],
]
b_w_f = [
    [WHITE, WHITE, BLACK, BLACK],
    [WHITE, WHITE, BLACK, BLACK],
    [WHITE, WHITE, BLACK, BLACK],
    [WHITE, WHITE, BLACK, EMPTY],
]

print(has_move(b_w_u, 1, 1))
print(has_move(b_w_f, 0, 3))
