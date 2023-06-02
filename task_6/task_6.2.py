import time

def even_number(num):
    return num % 2 == 0

start_time = time.time()
result = even_number(256)  # вызывается функция проверки числа на четность
end_time = time.time()

time_elapsed = end_time - start_time

filename = f"time_{time.strftime('%H:%M:%S %d.%m.%Y')}.txt"

with open(filename, 'w') as f:
    f.write(f"Время выполнения операции: {time_elapsed} секунд")

print(f"Время выполнения операции: {time_elapsed} секунд")
