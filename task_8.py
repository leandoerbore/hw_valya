text = '''
[Куплет 1]:
В истерике кружилась мама Валя
На заднем фоне замер папа Толя
В радиусе метра воцарился жесточайший хаос
Когда всем понятно стало: сын остался без диплома
Мама, не кричи, хватит плакать, не смей
Ты ж у меня ураган, а ураганы не плачут
И я подумаю, какую отмазу придумать
Ведь мой второй братан опять затеял что-то нехорошее

[Переход]:
Я подошёл к окну, посмотрел на свой двор
Пацаны курили, я им крикнул "Йо!"
Выбежал из дома и по пятницам исчезал
Я так хотел забыть уроки, но не забывал

[Припев]:
Я выбираю — жить в кайф!
Я выбираю — жить в кайф!
Я выбираю — жить в кайф!
Я выбираю — жить в кайф!

[Куплет 2]:
И это лето запомнится нам надолго
Нам было мало, и мы хотели ещё
Мы так любили жить, мы так хотели петь
И никто не смог нам запретить хотеть
И мы летели на свет, забыв про время и сон
Мы верили только ветру и, конечно, солнцу
Не замечая препятствий, летели просто на час
И вдруг увидел солнце — и тогда себе я сказал:

[Припев]:
Я выбираю — жить в кайф!
Я выбираю — жить в кайф!
Я выбираю — жить в кайф!
Я выбираю — жить в кайф!
'''

def main():
    while True:
        user_input = input("Введите номер задания (1-3) или 'выход' для завершения: ").strip()
        if user_input == 'выход':
            break
        elif user_input == '1':
            task_1()
        elif user_input == '2':
            task_2()
        elif user_input == '3':
            task_3()
        else:
            print("Неверный ввод. Пожалуйста, введите число от 1 до 3 или 'выход'.")

def task_1():
    # Разделяем текст песни на элементы
    song_parts = parse_song(text)
    # Отображаем варианты для вывода
    print("Доступные элементы песни:")
    for part_name in song_parts.keys():
        print(f"- {part_name}")
    # Запрашиваем у пользователя название элемента
    part_input = input("Введите название элемента песни для вывода: ").strip().lower()
    # Проверяем наличие элемента и выводим его текст
    part = find_song_part(song_parts, part_input)
    if part:
        print("\n" + part + "\n")
    else:
        print("Элемент песни не найден.")

def task_2():
    # Получаем текст песни без меток и выравниваем по центру
    song_lines = remove_labels(text)
    for line in song_lines:
        print(line.center(60))
    print("\n")

def task_3():
    # Запрашиваем у пользователя параметр подсчета слов
    option = input("Введите 'куплет' или 'песня': ").strip().lower()
    if option == 'куплет':
        getted_text = get_song_sections(text, ['куплет'])
    elif option == 'песня':
        getted_text = remove_labels(text)
    else:
        print("Неверный ввод. Пожалуйста, введите 'куплет' или 'песня'.")
        return
    # Подсчитываем частоту слов
    word_counts = count_words(getted_text)
    # Выводим 3 самых частых слова
    print_top_words(word_counts, 3)

def parse_song(text):
    import re
    # Разделяем текст на части с помощью регулярных выражений
    pattern = r'\[(.*?)\]:\n((?:.+\n)+)'
    matches = re.findall(pattern, text)
    song_parts = {}
    for title, lyrics in matches:
        song_parts[title.strip().lower()] = lyrics.strip()
    return song_parts

def find_song_part(song_parts, part_input):
    # Ищем часть песни по названию
    for part_name, lyrics in song_parts.items():
        if part_input == part_name.lower():
            return lyrics
    return None

def remove_labels(text):
    import re
    # Удаляем метки типа [Куплет 1]:
    pattern = r'\[.*?\]:\n'
    clean_text = re.sub(pattern, '', text)
    # Возвращаем список строк
    lines = clean_text.strip().split('\n')
    return lines

def get_song_sections(text, sections):
    import re
    # Получаем указанные части песни
    pattern = r'\[(.*?)\]:\n((?:.+\n)+)'
    matches = re.findall(pattern, text)
    selected_text = ''
    for title, lyrics in matches:
        lower_title = title.strip().lower()
        for section in sections:
            if section in lower_title:
                selected_text += lyrics + '\n'
    return selected_text.strip().split('\n')

def count_words(lines):
    import re
    from collections import Counter
    # Объединяем строки в один текст
    text = ' '.join(lines)
    # Приводим к нижнему регистру
    text = text.lower()
    # Удаляем специальные символы, кроме дефисов
    text = re.sub(r'[^\w\s-]', '', text)
    # Разделяем на слова
    words = text.split()
    words = [word for word in words if len(word) > 2]
    # Подсчитываем частоту слов
    word_counts = Counter(words)
    return word_counts

def print_top_words(word_counts, top_n):
    # Получаем top_n самых частых слов
    most_common = word_counts.most_common(top_n)
    for i, (word, count) in enumerate(most_common, 1):
        print(f"{i}. \"{word}\" - {count} раз")

if __name__ == '__main__':
    main()



# Your code here 𓆉𓆝 𓆟 𓆞 𓆝 𓆟𓇼
# Your code here 𓆉𓆝 𓆟 𓆞 𓆝 𓆟𓇼
# Your code here 𓆉𓆝 𓆟 𓆞 𓆝 𓆟𓇼
# Your code here 𓆉𓆝 𓆟 𓆞 𓆝 𓆟𓇼
