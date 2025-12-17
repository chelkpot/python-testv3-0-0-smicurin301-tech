# tasks/task2.py

def solve():
# Ниже пишите решение задачи
    # Задание 2. Электронные часы - 1
    n = int(input())
    n = n % 1440  # учитываем только текущие сутки
    hours = n // 60
    minutes = n % 60
    print(hours, minutes)
   

   
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()