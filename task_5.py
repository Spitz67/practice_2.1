import json
import os

data_file = "library.json"
available_file = "available_books.txt"


def load_library():
    if os.path.exists(data_file):
        with open(data_file, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
                if isinstance(data, list):
                    return data
                elif isinstance(data, dict):
                    return [data]
                else:
                    return []
            except json.JSONDecodeError:
                return []
    return []


def save_library(library):
    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump(library, f, ensure_ascii=False, indent=2)


def show_all_books(library):
    if not library:
        print("Библиотека пуста")
        return

    print("\nВсе книги в библиотеке:")
    for book in library:
        status = "Доступна" if book['available'] else "недоступна"
        print(f"ID: {book['id']}, {book['title']} - {book['author']} ({book['year']}) [{status}]")


def search_books(library):
    if not library:
        print("Библиотека пуста")
        return

    print("Поиск по: 1 - Автор, 2 - Название")
    search_type = input("Выберите тип поиска (1 или 2): ")

    if search_type == '1':
        query = input("Введите автора: ").lower()
        field = 'author'
    elif search_type == '2':
        query = input("Введите название: ").lower()
        field = 'title'
    else:
        print("Неверный выбор типа поиска")
        return

    results = []
    for book in library:
        if query in book[field].lower():
            results.append(book)

    if not results:
        print("Книги не найдены")
        return

    print(f"\nНайдено книг: {len(results)}")
    for book in results:
        status = "Доступна" if book['available'] else "недоступна"
        print(f"ID: {book['id']}, {book['title']} - {book['author']} ({book['year']}) [{status}]")


def add_book(library):
    if library:
        new_id = max(book['id'] for book in library) + 1
    else:
        new_id = 1

    title = input("Название книги: ").strip()
    author = input("Автор: ").strip()

    try:
        year = int(input("Год издания: "))
    except ValueError:
        print("Ошибка: год должен быть числом")
        return

    book = {
        'id': new_id,
        'title': title,
        'author': author,
        'year': year,
        'available': True
    }

    library.append(book)
    save_library(library)
    print(f"Книга '{title}' добавлена с ID: {new_id}")


def change_availability(library):
    if not library:
        print("Библиотека пуста")
        return

    try:
        book_id = int(input("Введите ID книги для изменения статуса: "))
    except ValueError:
        print("Ошибка: ID должен быть числом")
        return

    for book in library:
        if book['id'] == book_id:
            current_status = book['available']
            book['available'] = not current_status

            action = "возвращена" if current_status else "недоступна"
            save_library(library)
            print(f"Книга '{book['title']}' {action}")
            return

    print(f"Книга с ID {book_id} не найдена")


def delete_book(library):
    if not library:
        print("Библиотека пуста")
        return

    try:
        book_id = int(input("Введите ID книги для удаления: "))
    except ValueError:
        print("Ошибка: ID должен быть числом")
        return

    for i, book in enumerate(library):
        if book['id'] == book_id:
            deleted_title = book['title']
            library.pop(i)
            save_library(library)
            print(f"Книга '{deleted_title}' удалена")
            return

    print(f"Книга с ID {book_id} не найдена")


def export_available_books(library):
    available_books = [book for book in library if book['available']]

    if not available_books:
        print("Нет доступных книг для экспорта")
        return

    with open(available_file, 'w', encoding='utf-8') as f:
        f.write("Список доступных книг:\n")

        for book in available_books:
            f.write(f"ID: {book['id']}\n")
            f.write(f"Название: {book['title']}\n")
            f.write(f"Автор: {book['author']}\n")
            f.write(f"Год: {book['year']}\n")
            f.write("\n")

    print(f"Список экспортирован в файл: {available_file}")
    print(f"Доступных книг: {len(available_books)}")


def main():
    library = load_library()

    while True:
        print("\nСистема учета библиотечных книг")
        print("1. Просмотр всех книг")
        print("2. Поиск по автору/названию")
        print("3. Добавление новой книги")
        print("4. Изменение статуса доступности")
        print("5. Удаление книги по ID")
        print("6. Экспорт доступных книг в файл")
        print("7. Выход")

        choice = input("\nВыберите действие (1-7): ")

        if choice == '1':
            show_all_books(library)
        elif choice == '2':
            search_books(library)
        elif choice == '3':
            add_book(library)
        elif choice == '4':
            change_availability(library)
        elif choice == '5':
            delete_book(library)
        elif choice == '6':
            export_available_books(library)
        elif choice == '7':
            print("Выход из программы")
            break
        else:
            print("Неверный выбор")


if __name__ == "__main__":
    main()