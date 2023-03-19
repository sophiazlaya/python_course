import datetime

birthday_str = input("Введите дату своего рождения в формате ДД.ММ.ГГГГ: ")
birthday = datetime.datetime.strptime(birthday_str, "%d.%m.%Y").date()
today = datetime.date.today()

days_lived = (today - birthday).days
print(f"Вы прожили {days_lived} дней.")