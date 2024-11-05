from collections import Counter
import math

# Исходный текст
text = "четверть четверика гороха без червоточинки."

# Подсчет количества символов и вероятностей
char_count = Counter(text)
total_length = len(text)
char_prob = {char: count / total_length for char, count in char_count.items()}


# Функция для построения кода Шеннона
def shannon_code(char_prob):
    sorted_chars = sorted(char_prob.items(), key=lambda x: -x[1])
    codes = {}
    cumulative_prob = 0

    for char, prob in sorted_chars:
        code_length = math.ceil(-math.log2(prob))
        code = format(int(cumulative_prob * (2 ** code_length)), f'0{code_length}b')
        codes[char] = code
        cumulative_prob += prob

    return codes


# Построение кодов Шеннона
codes = shannon_code(char_prob)

# Вывод кодов
print("Коды Шеннона для символов:")
for char, code in codes.items():
    print(f"'{char}': {code}")

# Вычисление средней длины кода l для кода Шеннона
l_shannon = sum(char_prob[char] * len(codes[char]) for char in char_prob)

# Размер кодированной последовательности N для кода Шеннона
N_shannon = l_shannon * total_length

# Длина равномерного кода l_uniform (округляется до целого числа вверх)
M = len(char_prob)
l_uniform = math.ceil(math.log2(M))

# Размер кодированной последовательности N для равномерного кода
N_uniform = l_uniform * total_length

# Коэффициент сжатия κ для кода Шеннона
kappa_shannon = l_uniform / l_shannon

# Вывод результатов
print(f"\nСредняя длина кода Шеннона l: {l_shannon:.4f}")
print(f"Размер кодированной последовательности для кода Шеннона N: {N_shannon:.0f} бит")
print(f"Коэффициент сжатия для кода Шеннона κ: {kappa_shannon:.4f}")

# Вывод для равномерного кода
print(f"\nСредняя длина равномерного кода l_uniform: {l_uniform}")
print(f"Размер кодированной последовательности для равномерного кода N_uniform: {N_uniform:.0f} бит")
print(f"Коэффициент сжатия для равномерного кода κ (по определению): 1.0000")
