from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time


# Определение функции для выполнения задачи
def my_task(n):
    # Неблокирующая I/O-bound операция
    time.sleep(3)
    # Блокирующая CPU-bound операция
    # res = sum(a**3 for a in range(10_000_000))
    return f"Задача {n} выполнена"


def main():
    start = time.time()
    # Использование ThreadPoolExecutor для управления пулом потоков
    with ThreadPoolExecutor(max_workers=3) as executor:
        #вызывает join автоматически
        results = executor.map(my_task, range(3))  # Отправка задач на выполнение
        for result in results:
            print(f"ThreadPoolExecutor: {result}")
        print(f"Время выполнения трех задач в ThreadPoolExecutor: {time.time() - start:.3f} секунды")
    
    start = time.time()
    
    # Использование ProcessPoolExecutor для управления пулом процессов
    with ProcessPoolExecutor(max_workers=3) as executor:
        #вызывает join автоматически
        # BrokenProcessPool - один из процессов аварийно и всё падает
        results = executor.map(my_task, range(3, 6))  # Отправка задач на выполнение
        for result in results:
            print(f"ProcessPoolExecutor: {result}")
        print(f"Время выполнения трех задач в ProcessPoolExecutor: {time.time() - start:.3f} секунды")


if __name__ == '__main__':
    main()