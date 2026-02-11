import csv
import os


def read_products(filename='products.csv'):
    products = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['Цена'] = int(row['Цена'])
                row['Количество'] = int(row['Количество'])
                products.append(row)
    except FileNotFoundError:
        print(f"Файл {filename} не найден. Создан новый файл.")
    return products


def save_products(products, filename='products.csv'):
    with open(filename, 'w', encoding='utf-8', newline='') as file:
        fieldnames = ['Название', 'Цена', 'Количество']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(products)
    print(f"Данные сохранены в файл {filename}")


def add_product(products):
    print("\nДобавление нового товара")
    name = input("Введите название товара: ").strip()

    for product in products:
        if product['Название'].lower() == name.lower():
            print(f"Товар '{name}' уже существует!")
            update = input("Хотите обновить его данные? (да/нет): ").lower()
            if update == 'да':
                try:
                    product['Цена'] = int(input("Введите новую цену: "))
                    product['Количество'] = int(input("Введите новое количество: "))
                    print(f"Товар '{name}' обновлен!")
                except ValueError:
                    print("Ошибка: цена и количество должны быть числами!")
                return

    try:
        price = int(input("Введите цену товара: "))
        quantity = int(input("Введите количество товара: "))

        products.append({
            'Название': name,
            'Цена': price,
            'Количество': quantity
        })
        print(f"Товар '{name}' успешно добавлен!")
    except ValueError:
        print("Ошибка: цена и количество должны быть числами!")


def find_product(products):
    print("\nПоиск товара")
    name = input("Введите название товара для поиска: ").strip().lower()

    found = False
    for product in products:
        if product['Название'].lower() == name:
            print(f"\nНайден товар:")
            print(f"  Название: {product['Название']}")
            print(f"  Цена: {product['Цена']}")
            print(f"  Количество: {product['Количество']}")
            found = True
            break

    if not found:
        print(f"Товар '{name}' не найден.")


def calculate_total_value(products):
    total = 0
    for product in products:
        total += product['Цена'] * product['Количество']

    print(f"\nОбщая стоимость всех товаров")
    print(f"Стоимость: {total} руб.")
    return total


def display_products(products):
    print("\nСписок всех товаров")
    print(f"{'Название':<15} {'Цена':<10} {'Количество':<10} {'Стоимость':<15}")

    for product in products:
        value = product['Цена'] * product['Количество']
        print(f"{product['Название']:<15} {product['Цена']:<10} {product['Количество']:<10} {value:<10}")


def main():
    filename = 'products.csv'

    if not os.path.exists(filename):
        initial_data = [
            {'Название': 'Яблоки', 'Цена': 100, 'Количество': 50},
            {'Название': 'Бананы', 'Цена': 80, 'Количество': 30},
            {'Название': 'Молоко', 'Цена': 120, 'Количество': 20},
            {'Название': 'Хлеб', 'Цена': 40, 'Количество': 100}
        ]
        save_products(initial_data, filename)
        print(f"Создан файл {filename} с начальными данными.")

    products = read_products(filename)

    while True:
        print("\nУправление складом")
        print("1. Показать все товары")
        print("2. Добавить новый товар")
        print("3. Найти товар по названию")
        print("4. Рассчитать общую стоимость")
        print("5. Сохранить данные")
        print("6. Выйти из программы")

        choice = input("\nВыберите действие (1-6): ")

        if choice == '1':
            display_products(products)

        elif choice == '2':
            add_product(products)

        elif choice == '3':
            find_product(products)

        elif choice == '4':
            calculate_total_value(products)

        elif choice == '5':
            save_products(products, filename)
            break

        elif choice == '6':
            save = input("Сохранить изменения перед выходом? (да/нет): ").lower()
            if save == 'да':
                save_products(products, filename)
            print("До свидания!")
            break

        else:
            print("Неверный выбор. Пожалуйста, введите число от 1 до 6.")


if __name__ == "__main__":
    main()