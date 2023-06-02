from datetime import datetime, date

birthdate_input = input("Введите дату своего рождения в формате ДД.ММ.ГГГГ: ")
birthdate = datetime.strptime(birthdate_input, "%d.%m.%Y").date()

today = date.today()

days_lived = (today - birthdate).days


print(f"Вы прожили {days_lived} дней.")