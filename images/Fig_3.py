import matplotlib.pyplot as plt
import numpy as np

# Данные
sizes = ["4x4", "5x5", "6x6", "7x7", "8x8", "9x9", "10x10"]

times = {
    #"Python (+Numba)": [3.24, 3.97, 6.31, 28, 248, 2379, 21753],
    #"C (1 поток)": [0.06, 0.21, 1.08, 20.62, 234, 2379, 34366],
    "C (+OpenMP)": [0.06, 0.18, 0.45, 1.74, 9.58, 75, 1007],
    "CUDA": [0.112, 0.5, 1.942, 10.07, 50, 252, 2086],
}

# Построение логарифмического графика
plt.figure(figsize=(8, 6))

for label, time_values in times.items():
    time_values = [float(v) if v is not None else np.nan for v in time_values]
    plt.plot(sizes, time_values, marker='o', label=label)

# Настройки шрифтов
plt.xlabel("Количество спинов N", fontsize=19)
plt.ylabel("Время (с)", fontsize=19)

#plt.title("Сравнение времени перебора (логарифмическая шкала)", fontsize=26)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)

# Настройка легенды
plt.legend(fontsize=18)

plt.yscale("log")
plt.grid(True, linestyle="--", linewidth=0.5)
plt.show()
