def replace_artifacts(str):
    # Удаляем пробелы по побокам
    formattedStr = str.strip()

    # Замена '-' и пробелов на '_'
    formattedStr = formattedStr.replace('-', '_').replace(' ', '_')

    # Преобразование CamelCase в snake_case
    newFormattedStr = []
    for char in formattedStr:
        if char.isupper():
            if newFormattedStr and newFormattedStr[-1] != '_':
                newFormattedStr.append('_')
            newFormattedStr.append(char.lower())
        else:
            newFormattedStr.append(char)

    formattedStr = ''.join(newFormattedStr)

    # Замена избыточных '_' на один
    while '__' in formattedStr:
        formattedStr = formattedStr.replace('__', '_')

    while True:
        # Убираем лишние _ (в начале и в конце)
        if formattedStr[0] == '_':
            formattedStr = formattedStr[1:]
        if formattedStr[-1] == '_':
            formattedStr = formattedStr[:-1]
            
        # Удаление начальных цифр
        while formattedStr and formattedStr[0].isdigit():
            formattedStr = formattedStr[1:]
        
        if (formattedStr[0] != '_' and formattedStr[-1] != '_' and formattedStr[0].isdigit() == False):
            break

    # Убираем лишние _ (в начале и в конце)
    if formattedStr[0] == '_':
        formattedStr = formattedStr[1:]
    if formattedStr[-1] == '_':
        formattedStr = formattedStr[:-1]

    # Удаление начальных цифр
    while formattedStr and formattedStr[0].isdigit():
        formattedStr = formattedStr[1:]
    
    # Проверка на допустимые символы
    if not formattedStr.replace('_', '').isalnum():
        return "Введено некорректное имя переменной"

    return formattedStr

# test = '123123----___-123camselCase-123qweqwe'
# print(replace_artifacts(test))

user_input = input()
print(replace_artifacts(user_input))

# Примечание: выполнять данное задание с помощью функций выше необязательно, однако, возможно
# использование данных функций поможет вам на этапе размышлений о дизайне программы
# Your code here (˶ᵔ ᵕ ᵔ˶)