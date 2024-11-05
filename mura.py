from collections import Counter
import math

# Исходный текст
text = "четверть четверика гороха без червоточинки."

# Подсчет количества символов
char_count = Counter(text)
total_length = len(text)

# Вероятности появления символов
char_prob = {char: count / total_length for char, count in char_count.items()}

# Сортировка символов по вероятности (для построения кода Гилберта-Мура)
sorted_chars = sorted(char_prob.items(), key=lambda x: -x[1])

# Построение кодов Гилберта-Мура
codes = {}
code_length = 1
for i, (char, prob) in enumerate(sorted_chars):
    codes[char] = format(i, f'0{code_length}b')
    if i == (2 ** code_length) - 1:
        code_length += 1

# Вычисление средней длины кода
l = sum(char_prob[char] * len(codes[char]) for char in char_prob)

# Размер кодированной последовательности
N = l * total_length

# Длина равномерного кода
M = len(char_prob)
l_uniform = math.log2(M)

# Коэффициент сжатия
kappa = l_uniform / l

# Вывод результатов
print("Коды Гилберта-Мура для символов:")
for char, code in codes.items():
    print(f"'{char}': {code}")

print(f"\nСредняя длина кода l: {l:.4f}")
print(f"Размер кодированной последовательности N: {N:.0f} бит")
print(f"Коэффициент сжатия κ: {kappa:.4f}")
