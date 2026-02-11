def read_students(filename):
    students = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:
                    if ':' in line:
                        name, grades_str = line.split(':', 1)
                        try:
                            grades = list(map(int, grades_str.split(',')))
                            students.append((name.strip(), grades))
                        except ValueError:
                            print(f"Ошибка в формате оценок у студента: {name}")
                    else:
                        print(f"Некорректный формат строки: {line}")
    except FileNotFoundError:
        print(f"Ошибка: Файл '{filename}' не найден!")
    return students


def calculate_averages(students):
    results = []
    for name, grades in students:
        if grades:
            average = sum(grades) / len(grades)
            results.append((name, grades, average))
        else:
            print(f"У студента {name} нет оценок")
    return results


def write_top_students(results, filename, threshold=4.0):
    top_students = [student for student in results if student[2] > threshold]

    with open(filename, 'w', encoding='utf-8') as file:
        file.write("Студенты со средним баллом выше 4.0:\n")

        for name, grades, average in top_students:
            file.write(f"{name}: {grades} Cредний балл: {average:.2f}\n")

    return top_students, len(top_students)


def find_top_student(results):
    if not results:
        return None

    top_student = max(results, key=lambda x: x[2])
    return top_student


def print_statistics(results, top_student, top_count):

    if top_student:
        name, grades, average = top_student
        print(f"\nСтудент с наивысшим средним баллом:")
        print(f"{name}: {grades}")
        print(f"Средний балл: {average:.2f}")


def main():
    students = read_students('students.txt')

    if not students:
        print("Нет данных для обработки")
        return

    results = calculate_averages(students)
    top_students, top_count = write_top_students(results, 'result.txt')
    top_student = find_top_student(results)
    print_statistics(results, top_student, top_count)

    print("\nСодержимое файла result.txt:")
    with open('result.txt', 'r', encoding='utf-8') as f:
        print(f.read())


if __name__ == "__main__":
    main()