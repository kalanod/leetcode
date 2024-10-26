# Полезная нагрузка, которая может быть передана в одном фрагменте (с учётом заголовков)
packet_sizes = 1480

# Функция для вычисления количества фрагментов с учётом payload_size
def calculate_fragments_stepwise(packet_size, payload_size):
    if packet_size <= payload_size:
        return 1  # Если размер пакета меньше или равен полезной нагрузке, фрагментация не требуется
    return (packet_size + payload_size - 1) // payload_size  # Количество фрагментов с учётом полезной нагрузки

# Пересчёт количества фрагментов для заданных размеров пакетов
fragment_counts_stepwise = [calculate_fragments_stepwise(size, payload_size) for size in packet_sizes]

# Построение обновлённого ступенчатого графика
plt.figure(figsize=(8, 6))
plt.step(packet_sizes, fragment_counts_stepwise, where='post', marker='o', color='b', linestyle='-')

# Добавление подписей
plt.title('Количество фрагментов в зависимости от размера пакета (учёт полезной нагрузки = 1480 байт)')
plt.xlabel('Размер пакета (байты)')
plt.ylabel('Количество фрагментов')

# Отображение графика
plt.grid(True)
plt.show()
