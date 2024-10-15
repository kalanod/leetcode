def max_dance_width(S):
    pos = 0  # текущая позиция танца
    min_pos = 0  # минимальная достигнутая позиция
    max_pos = 0  # максимальная достигнутая позиция

    for ch in S:
        if ch == 'R':
            pos += 1
        elif ch == 'L':
            pos -= 1
        else:  # ch == '?'
            # Чтобы максимизировать ширину, заменяем '?' на 'R'
            pos += 1  # заменяем на R для максимальной ширины

        min_pos = min(min_pos, pos)
        max_pos = max(max_pos, pos)

    return max_pos - min_pos


# Пример
S = "R??L?"
print(max_dance_width(S))  # Ожидаемый результат: 3
