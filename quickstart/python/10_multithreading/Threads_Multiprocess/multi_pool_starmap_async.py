import time
from multiprocessing import Pool
import requests

# Асинхронная проверка доступности веб-сайтов с использованием callback-фунции.
# Функция для выполнения запросов
def check_url_status(url, timeout):
    print(f"Начало работы с {url}")
    response = requests.get(url, timeout=timeout)
    return f"{url=}: {response.status_code}"

# Функция обратного вызова, которая будет вызвана сразу, как только все задачи будут завершены
def callback_task(results):
    # Печать результатов работы
    for result in results:
        print(result)
        
def main():
    urls = [
        ("https://habr.com/ru/articles/789904/", 1), 
        ("https://ru.wikipedia.org/wiki/Параллельные_вычисления", 1),
        ("https://www.youtube.com/", 1),
        ("https://habr.com/ru/articles/865974/", 1)
    ]
    with Pool(5) as pool:
        # Отправляем задачи на выполнение в процессы
        result = pool.starmap_async(check_url_status, urls, callback=callback_task)
        # Пока идет обработка задач выполняем еще какую-то полезную работу
        # time.sleep(7)
        result.wait()  # Ожидание завершения всех задач
        print('Дальнейшее выполнение программы')

if __name__ == '__main__':
    main() # точка входа в программу