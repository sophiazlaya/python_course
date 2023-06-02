import time

while True:
    num = int(input("Введите число: "))
    if num > 0:
        print(f"Ждём {num} секунд...")
        time.sleep(num)
    else:
        print("Вы ввели отрицательное число. Выход из программы.")
        break

