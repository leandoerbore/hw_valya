# Инициализируем начальные координаты Петра
x = 0
y = 0

# Возможные направления
directions = ['Влево', 'Вправо', 'Вверх', 'Вниз']

# Считываем количество ходов
try:
    N = int(input("Введите N: "))
except ValueError:
    print("Некорректный ввод. Пожалуйста, введите целое число.")
    exit()

# Для каждого хода
for i in range(N):
    while True:
        direction = input(f"Ход {i+1}: ").strip()
        if direction not in directions:
            print("Неизвестное направление. Попробуйте снова.")
        else:
            # Обновляем координаты в зависимости от направления
            if direction == 'Вправо':
                x += 1
            elif direction == 'Влево':
                x -= 1
            elif direction == 'Вверх':
                y += 1
            elif direction == 'Вниз':
                y -= 1
            break  # Выходим из цикла, если направление корректно

# Вычисляем минимальное количество шагов до конечной точки
min_steps = abs(x) + abs(y)

# Выводим результат
print(min_steps)

# Your code here (˶ˆᗜˆ˵)