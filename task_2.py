# Определяем товары в автомате
products = {
    '001': {'name': 'Батончик', 'price': 70},
    '002': {'name': 'Вода', 'price': 45},
    '003': {'name': 'Газировка', 'price': 64},
    '004': {'name': 'Булочка', 'price': 33},
}

# Список допустимых купюр
valid_denominations = [10, 50, 100, 500]

# qwe

def print_table():
    # Выводим заголовок таблицы
    print('| {0:<3} | {1:<11} | {2:<4} |'.format('ID', 'ProductName', 'Цена'))
    print('|-----|-------------|------|')
    # Выводим каждую строку таблицы с данными товаров
    for product_id in sorted(products.keys()):
        data = products[product_id]
        print('| {0:<3} | {1:<11} | {2:<4} |'.format(product_id, data['name'], data['price']))
#edit# qwe q
def read_id(str_):
    if str_ == 'ОТМЕНА':
        return None
    if str_ not in products:
        print("Товара с таким ID не существует")
        return None
    else:
        return str_
    
# commit 2

def check_bill_validity(str_):
    if str_ == 'ОТМЕНА':
        return 'ОТМЕНА'
    try:
        denomination = int(str_)
        if denomination in valid_denominations:
            return denomination
        else:
            print("Внесена фальшивая купюра")
            return None
    except ValueError:
        print("Внесена фальшивая купюра")
        return None

def calculate_remaining(input_amount, amount_left):
    remaining = amount_left - input_amount
    if remaining <= 0:
        change = -remaining
        print(f"Ваша сдача: {change} тугриков")
        return 0
    else:
        print(f"Осталось внести {remaining} тугриков")
        return remaining

def main():
    # 1) Выводим таблицу товаров при запуске программы
    print_table()

    # 2) Просим пользователя ввести ID желаемого товара
    print('\nВведите ID желаемого товара\n')
    user_input = input()
    product_id = read_id(user_input)
    
    if product_id is None:
        return

    price = products[product_id]['price']
    remaining_price = price
    print(f"Внесите {price} тугриков")

    # 3) Начинаем принимать купюры от пользователя
    while remaining_price > 0:
        user_input = input()
        denomination = check_bill_validity(user_input)
        if denomination == 'ОТМЕНА':
            return
        elif denomination is None:
            continue
        else:
            # 4) Вычисляем оставшуюся суммуqwe
            remaining_price = calculate_remaining(denomination, remaining_price)
    # Выполнение программы завершается после внесения необходимой суммы

if __name__ == '__main__':
    main()

# Примечание: выполнять данное задание с помощью функций выше необязательно, однако, возможно
# использование данных функций поможет вам на этапе размышлений о дизайне программы
#qwe 
# Your code here(づ ᴗ _ᴗ)づ♡
#qwe

