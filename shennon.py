from collections import Counter
import math

# Исходная строка
text = "четверть четверика гороха без червоточинки."

# Шаг 1: Подсчет частот символов и вычисление вероятностей
symbol_frequencies = Counter(text)
total_symbols = len(text)
symbol_probabilities = {symbol: round(freq / total_symbols, 2) for symbol, freq in symbol_frequencies.items()}

# Шаг 2: Определение кумулятивной вероятности q(x) и построение кодов Шеннона
sorted_symbols = sorted(symbol_probabilities.items(), key=lambda item: item[1], reverse=True)
cumulative_probabilities = {}
shannon_codes = {}
code_lengths = {}

q = 0.0  # начальное значение кумулятивной вероятности
for symbol, p in sorted_symbols:
    cumulative_probabilities[symbol] = q
    l = math.ceil(-math.log2(p))  # длина кода для символа
    q_binary = int(q * (2**l))  # представление q в двоичной форме, длина l
    shannon_code = f"{q_binary:0{l}b}"  # двоичный код q с длиной l
    shannon_codes[symbol] = shannon_code
    code_lengths[symbol] = l
    q += p

# Шаг 3: Вычисление средней длины кода
average_code_length = sum(code_lengths[symbol] * p for symbol, p in symbol_probabilities.items())

# Шаг 4: Определение размера кодированной последовательности (N)
N = total_symbols * average_code_length

# Шаг 5: Вычисление коэффициента сжатия (κ)
uniform_code_length = math.ceil(math.log2(len(symbol_frequencies)))  # для равномерного кода
original_size = total_symbols * uniform_code_length
compression_ratio = original_size / N

# Форматированный вывод таблицы
print("Код Шеннона")
print("| x  | p(x)     | q(x)     | l(x) | q(x)_2   | c(x)       |")
print("|----|----------|----------|------|----------|------------|")
for symbol, p in symbol_probabilities.items():
    q = cumulative_probabilities[symbol]
    q_binary = f"{int(q * (2**code_lengths[symbol])):0{code_lengths[symbol]}b}"
    print(f"| {symbol}  | {p:.4f} | {q:.4f} | {code_lengths[symbol]}    | {q_binary}     | {shannon_codes[symbol]}       |")

# Вывод остальных значений
print(f"\nСредняя длина кода (l) = {average_code_length:.4f} бит")
print(f"Размер кодированной последовательности (N) = {N:.2f} бит")
print(f"Коэффициент сжатия (κ) = {compression_ratio:.4f}")
