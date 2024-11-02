from pulp import LpMaximize, LpProblem, LpVariable, lpSum

# Створюємо модель
model = LpProblem("Production_Optimization", LpMaximize)

# Визначаємо змінні
x = LpVariable("Lemonade", lowBound=0, cat="Integer")  # Кількість лимонаду
y = LpVariable("Fruit_Juice", lowBound=0, cat="Integer")  # Кількість фруктового соку

# Визначаємо функцію цілі (максимізація кількості вироблених продуктів)
model += x + y, "Total_Production"

# Додаємо обмеження на ресурси
model += 2 * x + y <= 100, "Water_Constraint"  # Вода
model += 1 * x <= 50, "Sugar_Constraint"       # Цукор
model += 1 * x <= 30, "Lemon_Juice_Constraint" # Лимонний сік
model += 2 * y <= 40, "Fruit_Puree_Constraint" # Фруктове пюре

# Розв'язуємо модель
model.solve()

# Виведення результатів
print("Результати оптимізації:")
print(f"Кількість лимонаду для виробництва: {x.varValue}")
print(f"Кількість фруктового соку для виробництва: {y.varValue}")
print(f"Максимальна кількість продуктів: {model.objective.value()}")