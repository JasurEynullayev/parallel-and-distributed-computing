from multiprocessing import Process
import time

# Fibonacci hesablayan funksiya
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Wrapper funksiya — sadəcə nəticəni çap edir
def hesapla_fibonacci(n):
    start = time.time()
    result = fibonacci(n)
    end = time.time()
    print(f"Fibonacci({n}) = {result} -- vaxt: {round(end - start, 2)} saniyə")

if __name__ == "__main__":
    fibonacci_numbers = [35, 34, 33, 32, 31]

    prosesler = []

    for n in fibonacci_numbers:
        p = Process(target=hesapla_fibonacci, args=(n,))
        prosesler.append(p)
        p.start()  # Prosesi işə sal

    for p in prosesler:
        p.join()  # Hamısını gözlə
