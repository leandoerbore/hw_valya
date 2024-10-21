# Список person
person = ['Энакин Скайуокер',
          41,
          ['Татуин', 'Набу', 'Джеонозис', 'Корусант', 'Мустафар', 'Звезда Смерти'],
          {'световой меч': 'синий', 'ранг': 'лорд ситхов'}
          ]

def task_1():
    # Вывести фамилию и имя в формате "Персона: {Фамилия}, {Имя}"
    full_name = person[0]
    names = full_name.strip().split()
    if len(names) >= 2:
        first_name, last_name = names[0], names[1]
    elif len(names) == 1:
        first_name = names[0]
        last_name = ''
    else:
        first_name = ''
        last_name = ''
    print(f"Персона: {last_name}, {first_name}")

def task_2():
    # Вывести возраст
    age = person[1]
    print(age)

def task_3():
    # Напечатать все места через запятую
    places = person[2]
    print(', '.join(places))

def task_4():
    # Вывести количество мест
    places = person[2]
    num_places = len(places)
    print(num_places)

def task_5():
    # Проверить, есть ли 'Звезда Смерти' среди мест
    places = person[2]
    serves_empire = 'Звезда Смерти' in places
    print(serves_empire)

def task_6():
    # Напечатать цвет светового меча
    attributes = person[3]
    saber_color = attributes.get('световой меч')
    print(saber_color)

def task_7():
    # Изменить возраст на 42 и вывести
    person[1] = 42
    print(person[1])

def task_8():
    # Добавить 'Эндор' в список мест (если его там нет) и вывести список
    places = person[2]
    if 'Эндор' not in places:
        places.append('Эндор')
    print(places)

def task_9():
    # Проверить ранг и вывести соответствующее сообщение
    attributes = person[3]
    rank = attributes.get('ранг', '')
    if rank == 'лорд ситхов':
        print('Энакин - лорд ситхов')
    else:
        print('Энакин - джедай')

def task_10():
    # Проверить количество мест и вывести сообщение
    places = person[2]
    if len(places) > 4:
        print('Энакин побывал во многих местах')
    else:
        print('Энакин не так много путешествовал')

def main():
    # Словарь для вызова функций по номеру задания
    task_functions = {
        '1': task_1,
        '2': task_2,
        '3': task_3,
        '4': task_4,
        '5': task_5,
        '6': task_6,
        '7': task_7,
        '8': task_8,
        '9': task_9,
        '10': task_10
    }
    
    while True:
        user_input = input()
        if user_input == 'выход':
            break
        if user_input in task_functions:
            task_functions[user_input]()
        else:
            print('Задание с таким номером не существует')

if __name__ == '__main__':
    main()

# Примечание: выполнять данное задание с помощью функций выше необязательно, однако, возможно
# использование данных функций поможет вам на этапе размышлений о дизайне программы
# Your code here /ᐠ˵- ⩊ -˵マ
