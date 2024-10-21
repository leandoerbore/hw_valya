# Список доступных предметов
available_items = ['меч', 'лук', 'топор', 'щит', 'зелье']

def process_items(str_):
    # Приводим строку к нижнему регистру и разбиваем на предметы
    selected_items = str_.strip().lower().split()
    # Проверяем, что количество предметов от 1 до 3
    if not (1 <= len(selected_items) <= 3):
        print("Вы должны выбрать минимум 1 и максимум 3 предмета.")
        return None
    # Проверяем, что все выбранные предметы допустимы
    invalid_items = [item for item in selected_items if item not in available_items]
    if invalid_items:
        print("Неверный предмет, попробуйте снова")
        return None
    # Возвращаем множество выбранных предметов
    return set(selected_items)

def main():
    # Список для хранения наборов предметов от каждого авантюриста
    adventurers_choices = []
    # Для каждого из 3 авантюристов
    for i in range(1, 4):
        while True:
            print(f"Авантюрист {i}, выберите от 1 до 3 предметов из списка (меч, лук, топор, щит, зелье):")
            input_items = input()
            adventurer_items = process_items(input_items)
            if adventurer_items is not None:
                adventurers_choices.append(adventurer_items)
                break
            # Иначе предлагаем ввести предметы заново
    # Находим пересечение выборов всех авантюристов
    common_items = set.intersection(*adventurers_choices)
    # Выводим количество предметов, которые войдут в общий набор
    print(f"Количество предметов, которые войдут в общий набор: {len(common_items)}")

if __name__ == '__main__':
    main()

# Your code here (づ｡◕‿‿◕｡)づ