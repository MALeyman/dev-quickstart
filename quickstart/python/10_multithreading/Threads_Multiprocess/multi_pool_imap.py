from multiprocessing.pool import Pool, ThreadPool
import requests
import time
import random

# Параллельная загрузка веб-страниц

def load_url(url):
    """Загружает содержимое по URL и возвращает его размер."""
    # Имитация задержки загрузки
    # time.sleep(random.randint(1, 3))  # Задержка от 1 до 3 секунд
    response = requests.get(url)
    # print(f"Загружено {url}, размер: {len(response.content)} байт")
    print(f"Загружено, размер: {len(response.content)} байт")
    return len(response.content), url

def check_url(url):
    try:
        response = requests.head(url, timeout=5)
        return url, response.status_code
    except requests.RequestException:
        return url, "Ошибка"

urls = [
    "http://www.example.com",
    "http://www.python.org",
    "http://www.google.com"
]
urls_habr_wiki = [
    "https://habr.com/ru/articles/789904/",
    "https://notebooks.githubusercontent.com/view/ipynb?browser=unknown_browser&bypass_fastly=true&color_mode=auto&commit=dd22d79fd1bb2319e3a41917990001ac89bc1e7f&device=unknown_device&docs_host=https%3A%2F%2Fdocs.github.com&enc_url=68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f6d6c636f757273656d6d2f707932303231617574756d6e2f646432326437396664316262323331396533613431393137393930303031616338396263316537662f507974686f6e30392d506172616c6c656c2e6970796e62&logged_in=false&nwo=mlcoursemm%2Fpy2021autumn&path=Python09-Parallel.ipynb&platform=unknown_platform&repository_id=413145534&repository_type=Repository&version=0",
    "https://habr.com/ru/articles/865974/"
]

if __name__ == '__main__':
    start_time = time.time()
    with ThreadPool(4) as pool:
        print("Загрузка веб-страниц...")
        for size in pool.imap(load_url, urls_habr_wiki):
            # сохранение порядка
            elapsed_time = time.time() - start_time
            print(f"Обработано за {elapsed_time:.2f} сек. Размер страницы: {size[0]} байт {size[1]}")
    
    start_time = time.time()
    with ThreadPool(4) as pool:
        # for url, status in pool.imap_unordered(load_url, urls_habr_wiki):
        for size in pool.imap_unordered(load_url, urls_habr_wiki):
            elapsed_time = time.time() - start_time
            # print(f"Обработано за {elapsed_time:.2f} сек. {url}: {status}")
            print(f"Обработано за {elapsed_time:.2f} сек. {size}")