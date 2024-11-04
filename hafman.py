from heapq import heappush, heappop, heapify
from collections import Counter
import math

# Исходная строка
text = "четверть четверика гороха без червоточинки."

# Шаг 1: Подсчет частот символов
symbol_frequencies = Counter(text)
total_symbols = len(text)

# Подсчет вероятностей для каждого символа
symbol_probabilities = {symbol: freq / total_symbols for symbol, freq in symbol_frequencies.items()}

# Шаг 2: Построение дерева Хаффмана и получение кодов
# Строим дерево Хаффмана
heap = [[weight, [symbol, ""]] for symbol, weight in symbol_frequencies.items()]
heapify(heap)

while len(heap) > 1:
    lo = heappop(heap)
    hi = heappop(heap)
    for pair in lo[1:]:
        pair[1] = '0' + pair[1]
    for pair in hi[1:]:
        pair[1] = '1' + pair[1]
    heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

# Получение кодов Хаффмана для каждого символа
huffman_codes = sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))
huffman_dict = {symbol: code for symbol, code in huffman_codes}

# Форматированный вывод таблицы
print("Код Хаффмана")
print("| x  | p(x)     | c(x)       | l(x) |")
print("|----|----------|------------|------|")
for symbol, code in huffman_dict.items():
    probability = symbol_probabilities[symbol]
    code_length = len(code)
    print(f"| {symbol}  | {probability:.4f} | {code}       | {code_length}   |")
