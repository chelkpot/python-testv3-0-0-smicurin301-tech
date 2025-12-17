# tasks/task5.py

def solve():
# Ниже пишите решение задачи
    # Задание 5. Электронные часы - 2
    n = int(input())

    # Оставляем только секунды текущих суток
    n = n % 86400

    hours = n // 3600
    minutes = (n % 3600) // 60
    seconds = n % 60

    # Форматируем вывод
    print(f"{hours}:{minutes:02d}:{seconds:02d}")

   
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()