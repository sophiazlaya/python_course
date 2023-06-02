import time

start_time = time.time()

print("Выполняем какую-то операцию...")
time.sleep(3)

end_time = time.time()

elapsed_time = end_time - start_time
print(f"Время выполнения операции: {elapsed_time} секунд.")

filename = time.strftime("result.txt")
with open("result.txt", "w", encoding='utf-8') as f:
    f.write(f"Время выполнения операции: {elapsed_time} секунд.")
    print("Время выполнения операции сохранено в файле 'result.txt'")