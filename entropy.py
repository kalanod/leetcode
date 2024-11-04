from collections import Counter
import math

# Исходный текст
text = "четверть четверика гороха без червоточинки. "

# Подсчет частоты каждого символа
char_counts = Counter(text)

# Общее количество символов
total_chars = len(text)

# Вывод частот символов
print("Частота символов:")
for char, count in char_counts.items():
    print(f"Символ: '{char}', Частота: {count}")

# Вычисление вероятностей и энтропии
entropy = 0.0
print("\nВероятности и значения -p(x_i) * log2(p(x_i)):")
for char, count in char_counts.items():
    p = round(count / total_chars, 2)  # вероятность, округленная до 4 знаков
    entropy_contribution = -round(p * math.log2(p), 2) if p > 0 else 0  # вклад в энтропию, округленный до 4 знаков
    entropy += entropy_contribution  # суммируем вклад
    print(f"Символ: '{char}', Вероятность: {p:.2f}, Вклад: {entropy_contribution:.2f}")

# Округление результата до двух знаков после запятой
entropy = round(entropy, 2)

# Вывод конечного результата
print(f"\nОдномерная энтропия H(X): {entropy:.2f}")
print(len("четверть четверика гороха без червоточинки."))