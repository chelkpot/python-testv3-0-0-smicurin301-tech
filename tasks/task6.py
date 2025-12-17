# Бонусная часть
# Задание №1 Плоскоземельщики
x = int(input())

# Диаметр тарелкоподобной планеты (2 радиуса)
diameter = 2 * x

# Расстояние перелета равно диаметру
# Скорость ИЛ-96: 900 км/ч
# Время = расстояние / скорость
time_hours = diameter / 900

# Округляем до ближайшего целого числа часов
rounded_time = int(time_hours + 0.5)  # округление вверх при .5 и больше

print(diameter, rounded_time)

# Задание №2 Шифр данных
X = input()

# Преобразуем каждую цифру в число
digits = [int(d) for d in X]

# Шаг 1: (цифра + 7) % 10
digits = [(d + 7) % 10 for d in digits]

# Шаг 2: меняем местами первую и третью цифры
digits[0], digits[2] = digits[2], digits[0]

# Шаг 3: меняем местами вторую и четвертую цифры
digits[1], digits[3] = digits[3], digits[1]

# Формируем результат
result = digits[0] * 1000 + digits[1] * 100 + digits[2] * 10 + digits[3]
print(result)