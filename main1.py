import datetime

def get_user_birthday():
    day = int(input("Введите день вашего рождения (дд): "))
    month = int(input("Введите месяц вашего рождения (мм): "))
    year = int(input("Введите год вашего рождения (гггг): "))
    return day, month, year

def get_day_of_week(day, month, year):
    date = datetime.date(year, month, day)
    days_of_week = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    return days_of_week[date.weekday()]

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def calculate_age(day, month, year):
    today = datetime.date.today()
    birthday = datetime.date(year, month, day)
    age = today.year - birthday.year
    if today < birthday.replace(year=today.year):
        age -= 1
    return age

def get_years_word(years):
    if 11 <= years % 100 <= 14:
        return "лет"
    elif years % 10 == 1:
        return "год"
    elif 2 <= years % 10 <= 4:
        return "года"
    else:
        return "лет"

def print_date_in_stars(day, month, year):
    numbers = {
        '0': [" *** ",
              "*   *",
              "*   *",
              "*   *",
              " *** "],
        '1': ["  *  ",
              " **  ",
              "  *  ",
              "  *  ",
              " *** "],
        '2': [" *** ",
              "*   *",
              "   * ",
              "  *  ",
              "*****"],
        '3': [" *** ",
              "*   *",
              "   **",
              "*   *",
              " *** "],
        '4': ["   * ",
              "  ** ",
              " * * ",
              "*****",
              "   * "],
        '5': ["*****",
              "*    ",
              "**** ",
              "    *",
              "**** "],
        '6': [" *** ",
              "*    ",
              "**** ",
              "*   *",
              " *** "],
        '7': ["*****",
              "   * ",
              "  *  ",
              " *   ",
              "*    "],
        '8': [" *** ",
              "*   *",
              " *** ",
              "*   *",
              " *** "],
        '9': [" *** ",
              "*   *",
              " ****",
              "    *",
              " *** "]
    }
    
    date_str = f"{day:02d} {month:02d} {year}"
    rows = [""] * 5
    for char in date_str:
        if char == ' ':
            for i in range(5):
                rows[i] += "   "
        else:
            for i in range(5):
                rows[i] += numbers[char][i] + " "
    for row in rows:
        print(row)

if __name__ == "__main__":
    day, month, year = get_user_birthday()
    print(f"Вы родились: {day:02d}.{month:02d}.{year}")
    print(f"Это был день недели: {get_day_of_week(day, month, year)}")
    print(f"Это был {'високосный' if is_leap_year(year) else 'обычный'} год.")
    age = calculate_age(day, month, year)
    print(f"Вам сейчас {age} {get_years_word(age)}.")
    print("Дата вашего рождения в формате электронного табло:")
    print_date_in_stars(day, month, year)
