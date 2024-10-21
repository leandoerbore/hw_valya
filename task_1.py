def replace_artifacts(str):
    # Удаляем пробелы по побокам
    formatted_str = str.strip()

    # Замена '-' и пробелов на '_'
    formatted_str = formatted_str.replace('-', '_').replace(' ', '_')

    # Преобразование CamelCase в snake_case
    new_formatted_str = []
    for char in formatted_str:
        if char.isupper():
            if new_formatted_str and new_formatted_str[-1] != '_':
                new_formatted_str.append('_')
            new_formatted_str.append(char.lower())
        else:
            new_formatted_str.append(char)

    formatted_str = ''.join(new_formatted_str)

    # Замена избыточных '_' на один
    while '__' in formatted_str:
        formatted_str = formatted_str.replace('__', '_')

    while True:
        # Убираем лишние _ (в начале и в конце)
        if formatted_str[0] == '_':
            formatted_str = formatted_str[1:]
        if formatted_str[-1] == '_':
            formatted_str = formatted_str[:-1]
            
        # Удаление начальных цифр
        while formatted_str and formatted_str[0].isdigit():
            formatted_str = formatted_str[1:]
        
        if (formatted_str[0] != '_' and formatted_str[-1] != '_' and formatted_str[0].isdigit() == False):
            break

    # Убираем лишние _ (в начале и в конце)
    if formatted_str[0] == '_':
        formatted_str = formatted_str[1:]
    if formatted_str[-1] == '_':
        formatted_str = formatted_str[:-1]

    # Удаление начальных цифр
    while formatted_str and formatted_str[0].isdigit():
        formatted_str = formatted_str[1:]
    
    # Проверка на допустимые символы
    if not formatted_str.replace('_', '').isalnum():
        return "Введено некорректное имя переменной"

    return formatted_str

test = '123123----___-123camselCase-123qweqwe'
print(replace_artifacts(test))

# user_input = input()
# print(replace_artifacts(user_input))

# Примечание: выполнять данное задание с помощью функций выше необязательно, однако, возможно
# использование данных функций поможет вам на этапе размышлений о дизайне программы
# Your code here (˶ᵔ ᵕ ᵔ˶)