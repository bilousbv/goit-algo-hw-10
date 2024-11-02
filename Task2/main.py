import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Визначення функції
def f(x):
    return x ** 2

# Межі інтегрування
a = 0
b = 2

# Метод Монте-Карло для обчислення інтегралу
def monte_carlo_integration(func, a, b, n_points):
    x_random = np.random.uniform(a, b, n_points)
    y_random = func(x_random)
    integral = (b - a) * np.mean(y_random)
    return integral

# Кількість точок для методу Монте-Карло
n_points = 10000
monte_carlo_result = monte_carlo_integration(f, a, b, n_points)

# Використання функції quad для аналітичного розрахунку інтегралу
quad_result, error = spi.quad(f, a, b)

# Виведення результатів
print("Метод Монте-Карло:", monte_carlo_result)
print("Метод quad:", quad_result)
print("Абсолютна похибка:", abs(monte_carlo_result - quad_result))

# Побудова графіка
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()