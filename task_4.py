import datetime

log_file = "calculator.log"


def show_last_operations():
    try:
        with open(log_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            if lines:
                print("\nПоследние 5 операций:")
                for line in lines[-5:]:
                    print(line.strip())
            else:
                print("\nЛог-файл пуст")
    except FileNotFoundError:
        print("\nЛог-файл не найден")


def clear_log():
    try:
        with open(log_file, 'w', encoding='utf-8') as f:
            pass
        print("\nЛог-файл очищен")
    except Exception as e:
        print(f"\nОшибка при очистке лог-файла: {e}")


def log_operation(operation, result):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, 'a', encoding='utf-8') as f:
        f.write(f"[{timestamp}] {operation} = {result}\n")


def calculator():
    while True:
        print("\n1. Калькулятор")
        print("2. Показать последние 5 операций")
        print("3. Очистить лог-файл")
        print("4. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            try:
                num1 = float(input("Введите первое число: "))
                num2 = float(input("Введите второе число: "))
                operation = input("Введите операцию (+, -, *, /): ")

                if operation == '+':
                    result = num1 + num2
                elif operation == '-':
                    result = num1 - num2
                elif operation == '*':
                    result = num1 * num2
                elif operation == '/':
                    if num2 == 0:
                        print("\nОшибка: деление на ноль!")
                        continue
                    result = num1 / num2
                else:
                    print("\nОшибка: неверная операция!")
                    continue

                operation_str = f"{num1} {operation} {num2}"
                print(f"Результат: {operation_str} = {result}")

                log_operation(operation_str, result)

            except ValueError:
                print("\nОшибка: введите числа корректно!")
            except Exception as e:
                print(f"Произошла ошибка: {e}")

        elif choice == '2':
            show_last_operations()

        elif choice == '3':
            clear_log()

        elif choice == '4':
            print("Выход из программы")
            break

        else:
            print("\nНеверный выбор!")


if __name__ == "__main__":
    calculator()