# Paralel və Asinxron Proqramlaşdırma Nümunələri — Python

# ---------------------------------------
# Fibonacci (normal metod)
# ---------------------------------------
import time

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

start_time = time.time()
fibonacci_numbers = [35, 34, 33, 32, 31]

for num in fibonacci_numbers:
    print(f"Fibonacci({num}) = {fibonacci(num)}")

finish_time = time.time()
print("Tam vaxt:", finish_time - start_time, "saniyə")


# ---------------------------------------
# Fibonacci (multiprocessing ilə)
# ---------------------------------------
import multiprocessing
import time

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def calculate_fibonacci(n):
    result = fibonacci(n)
    print(f"Fibonacci({n}) = {result}")

if __name__ == "__main__":
    start_time = time.time()
    fibonacci_numbers = [35, 34, 33, 32, 31]
    processes = []

    for num in fibonacci_numbers:
        process = multiprocessing.Process(target=calculate_fibonacci, args=(num,))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()

    finish_time = time.time()
    print("Tüm işlemler tamamlandı.")
    print("Tam vaxt:", finish_time - start_time, "saniyə")


# ---------------------------------------
# Kvadrat Hesablama (normal metod)
# ---------------------------------------
import random
import time

def calculate_square(num):
    time.sleep(0.1)
    return num ** 2

start_time = time.time()
random_numbers = [random.randint(10000, 100000) for _ in range(200)]
results = [calculate_square(num) for num in random_numbers]

print("Kvadrat nəticələr:", results)
print("Tam vaxt:", time.time() - start_time, "saniyə")


# ---------------------------------------
# Kvadrat Hesablama (multiprocessing + Pool)
# ---------------------------------------
import multiprocessing
import random
import time

def calculate_square(num):
    time.sleep(0.1)
    return num ** 2

if __name__ == "__main__":
    start_time = time.time()
    random_numbers = [random.randint(10000, 100000) for _ in range(200)]

    with multiprocessing.Pool() as pool:
        results = pool.map(calculate_square, random_numbers)

    print("Kvadrat nəticələr:", results)
    print("Tam vaxt:", time.time() - start_time, "saniyə")


# ---------------------------------------
# Asinxron Davranış (asyncio ilə)
# ---------------------------------------
import asyncio
import time

async def other(id, t):
    await asyncio.sleep(t)
    print(f"Mən coroutine-{id}-əm")

async def main():
    task1 = asyncio.create_task(other(1, 10))
    task2 = asyncio.create_task(other(2, 4))
    task3 = asyncio.create_task(other(3, 1))
    await task1
    await task2
    await task3

start_time = time.time()
asyncio.run(main())
print("Tam vaxt:", time.time() - start_time, "saniyə")


# ---------------------------------------
# Sinxron Davranış (adi metod)
# ---------------------------------------
import time

def other(id, t):
    time.sleep(t)
    print(f"Mən coroutine-{id}-əm")

def main():
    other(1, 10)
    other(2, 4)
    other(3, 1)

start_time = time.time()
main()
print("Tam vaxt:", time.time() - start_time, "saniyə")


# ---------------------------------------
# Queue ilə Paralel Proseslərarası Əlaqə
# ---------------------------------------
import multiprocessing
import time

def writer(queue):
    for i in range(5):
        msg = f"Mesaj {i}"
        queue.put(msg)
        print(f"Yazıldı: {msg}")
        time.sleep(1)

def reader(queue):
    while True:
        msg = queue.get()
        print(f"Oxundu: {msg}")
        if msg == "Mesaj 4":
            break

if __name__ == "__main__":
    queue = multiprocessing.Queue()
    writer_process = multiprocessing.Process(target=writer, args=(queue,))
    reader_process = multiprocessing.Process(target=reader, args=(queue,))
    
    writer_process.start()
    reader_process.start()
    
    writer_process.join()
    reader_process.join()
    
    print("Məlumat mübadiləsi tamamlandı.")


# ---------------------------------------
# Səhv: Proseslərarası Paylaşılmayan List
# ---------------------------------------
import multiprocessing
import time

shared_data = []

def writer():
    for i in range(5):
        shared_data.append(f"Mesaj {i}")
        print(f"Yazıldı: Mesaj {i}")
        time.sleep(1)

def reader():
    time.sleep(2)
    for msg in shared_data:
        print(f"Oxundu: {msg}")

if __name__ == "__main__":
    writer_process = multiprocessing.Process(target=writer)
    reader_process = multiprocessing.Process(target=reader)

    writer_process.start()
    reader_process.start()

    writer_process.join()
    reader_process.join()

    print("Məlumat mübadiləsi tamamlandı.")
