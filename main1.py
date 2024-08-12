from datetime import datetime

# Функция для определения дня недели
def get_weekday(day, month, year):
    date = datetime(year, month, day)
    days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    return days[date.weekday()]

# Функция для определения, является ли год високосным
def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# Функция для определения возраста пользователя
def calculate_age(day, month, year):
    today = datetime.today()
    birthdate = datetime(year, month, day)
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

# Функция для стилистического преобразования даты рождения
def convert_date_to_stars(date_str):
    # Определяем отображение каждой цифры
    digits = {
        '0': ["***", "* *", "* *", "* *", "***"],
        '1': ["  *", "  *", "  *", "  *", "  *"],
        '2': ["***", "  *", "***", "*  ", "***"],
        '3': ["***", "  *", "***", "  *", "***"],
        '4': ["* *", "* *", "***", "  *", "  *"],
        '5': ["***", "*  ", "***", "  *", "***"],
        '6': ["***", "*  ", "***", "* *", "***"],
        '7': ["***", "  *", "  *", "  *", "  *"],
        '8': ["***", "* *", "***", "* *", "***"],
        '9': ["***", "* *", "***", "  *", "***"]
    }
    
    # Разделяем строки для формирования цифр
    lines = ["", "", "", "", ""]
    
    # Проходим по каждому символу в строке даты
    for char in date_str:
        if char == " ":
            for i in range(5):
                lines[i] += "   "  # Добавляем пробел между блоками цифр
        elif char in digits:
            for i in range(5):
                lines[i] += digits[char] + "  "  # Добавляем прорисованную цифру
    
    # Возвращаем результат как единую строку
    return "\n".join(lines)
        print(line)

# Ввод данных пользователя
day = int(input("Введите день вашего рождения: "))
month = int(input("Введите месяц вашего рождения: "))
year = int(input("Введите год вашего рождения: "))

# Вывод информации
print(f"Вы родились в {get_weekday(day, month, year)}.")
print(f"{year} год {'високосный' if is_leap_year(year) else 'не високосный'}.")
print(f"Вам сейчас {calculate_age(day, month, year)} лет.")

print("\nДата рождения в стиле электронного табло:")
print_styled_date(day, month, year)