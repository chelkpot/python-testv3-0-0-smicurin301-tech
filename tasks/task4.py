# tasks/task4.py

def solve():
# Ниже пишите решение задачи
    # Задание 4. Следующее четное
    n = int(input())
    # Формула: (n + 2) // 2 * 2
    next_even = ((n // 2) + 1) * 2
    print(next_even)    

    

# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()