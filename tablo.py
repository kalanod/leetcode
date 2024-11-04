def identify_letter(n, board):
    # Словарь для хранения координат углов по типам
    corners = {'top_left': [], 'top_right': [], 'bottom_left': [], 'bottom_right': []}

    # Функция для определения типа угла на основе его соседей
    def determine_corner_type(x, y):
        types = []
        if x > 0 and y > 0 and board[x - 1][y] == '.' and board[x][y - 1] == '.':
            types.append('top_left')
        if x > 0 and y < n - 1 and board[x - 1][y] == '.' and board[x][y + 1] == '.':
            types.append('top_right')
        if x < n - 1 and y > 0 and board[x + 1][y] == '.' and board[x][y - 1] == '.':
            types.append('bottom_left')
        if x < n - 1 and y < n - 1 and board[x + 1][y] == '.' and board[x][y + 1] == '.':
            types.append('bottom_right')
        return types

    # Проход по всем горящим пикселям и добавление их в углы, если они подходят
    for i in range(n):
        for j in range(n):
            if board[i][j] == '#':
                corner_types = determine_corner_type(i, j)
                for corner_type in corner_types:
                    corners[corner_type].append((i, j))

    # Карты для каждой буквы (на основе относительных позиций углов)
    letter_maps = {
        'O': {
            'top_left': 1, 'top_right': 1, 'bottom_left': 1, 'bottom_right': 1
        },
        'C': {
            'top_left': 1, 'top_right': 1, 'bottom_left': 1, 'bottom_right': 0
        },
        'L': {
            'top_left': 1, 'top_right': 0, 'bottom_left': 1, 'bottom_right': 1
        },
        'I': {
            'top_left': 0, 'top_right': 0, 'bottom_left': 0, 'bottom_right': 0
        },
        'H': {
            'top_left': 1, 'top_right': 1, 'bottom_left': 1, 'bottom_right': 1
        },
        'P': {
            'top_left': 1, 'top_right': 1, 'bottom_left': 1, 'bottom_right': 1
        }
    }

    # Проверка на соответствие картам букв
    def match_letter(corner_counts):
        for letter, map_corners in letter_maps.items():
            match = True
            for corner_type, count in map_corners.items():
                if len(corners[corner_type]) != count:
                    match = False
                    break
            if match:
                return letter
        return 'X'

    # Получаем количество углов для каждой буквы
    return match_letter(corners)


# Ввод данных
n = int(input())
board = [input().strip() for _ in range(n)]
print(identify_letter(n, board))
