def season(moth):

    if month == 12 or month < 3:
        return "Зима"
    elif month == 3 or month < 6:
        return "Весна"
    elif month == 6 or month < 9:
        return "Лето"
    else:
        return "Осень"



month = input("Введите месяц(число):")



month = int(month)
while True:
    if month == 0:
        print("Такого месяца не существует."
              " Используйте целые числа")
        month = input("Введите месяц(число):")
        continue
    else:
        break


answer = season(month)
print(answer)