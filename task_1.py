
with open('text.txt', 'w+', encoding='utf-8') as file:
    lines_to_write = [
        file.write(f"Первая строка\n"),
        file.write(f"Вторая строка\n"),
        file.write(f"Третья строка\n"),
        file.write(f"Четвертая строка\n"),
        file.write(f"Пятая строка\n")
    ]

with open('text.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

    line_count = len(lines)
    print(f"Количество строк в файле: {line_count}")

    word_count = 0
    for line in lines:
        words = line.split()
        word_count += len(words)
    print(f"Количество слов в файле: {word_count}")

    longest_line = max(lines, key=len)
    print(f"Самая длинная строка: '{longest_line}'")
    print(f"Длина самой длинной строки: {len(longest_line)} символов")
