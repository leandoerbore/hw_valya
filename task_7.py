def reverse_number(n):
    isAbsed = False
    if n < 0:
        n = abs(n)
        isAbsed = True

    if n >= 0 and n <= 9:
        return n

    reversed_number = 0
    # Отбрасываем конечные нули в исходном числе
    while n % 10 == 0 and n != 0:
        n = n // 10

    # Разворачиваем число
    while n != 0:
        digit = n % 10
        reversed_number = reversed_number * 10 + digit
        n = n // 10

    # Специальная проверка для случая, когда число становится 1 после разворота
    if reversed_number >= 0 and reversed_number <= 9 :
        return 0
    else:
        if (isAbsed):
            return -reversed_number
        else:
            return reversed_number

# Считываем число с клавиатуры
try:
    N = int(input("Ввод: "))
    result = reverse_number(N)
    print(f"Вывод: {result}")
except ValueError:
    print("Некорректный ввод. Пожалуйста, введите целое число.")

# Your code here (づ๑•ᴗ•๑)づ♡