def replace_artifacts(str):
    # Удаляем пробелы по побокам
    formattedStr = str.strip()

    # Замена '-' и пробелов на '_'
    formattedStr = formattedStr.replace('-', '_').replace(' ', '_')

    # Замена избыточных '_' на один
    while '__' in formattedStr:
        formattedStr = formattedStr.replace('__', '_')

    # Удаление начальных цифр
    newFormattedStr = []
    for char in formattedStr:
        if char.isupper():
            if newFormattedStr and newFormattedStr[-1] != '_':
                newFormattedStr.append('_')
            newFormattedStr.append(char.lower())
        else:
            newFormattedStr.append(char)

    formattedStr = ''.join(newFormattedStr)

    # Удаление начальных цифр
    while newFormattedStr and newFormattedStr[0].isdigit():
        newFormattedStr = newFormattedStr[1:]
    
    # Проверка на допустимые символы
    # if not newFormattedStr.replace('_', '').join('').isalnum():
    #     return "Введено некорректное имя переменной"


    return formattedStr

# test = '1Python-Qweqw'
user_input = input()
print(replace_artifacts(user_input))
# print(replace_artifacts(test))

# Примечание: выполнять данное задание с помощью функций выше необязательно, однако, возможно
# использование данных функций поможет вам на этапе размышлений о дизайне программы
# Your code here (˶ᵔ ᵕ ᵔ˶)
