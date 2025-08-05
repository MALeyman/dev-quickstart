from multiprocessing.pool import Pool, ThreadPool
import requests

# Параллельное извлечение данных из URL

def fetch_url(url):
    response = requests.get(url)
    return f"Содержимое {url}: {len(response.content)} символов"

urls = [
    "http://example.com",
    "http://example.org",
    "http://example.net"
]
urls_habr_wiki = [
    "https://habr.com/ru/articles/789904/",
    "https://ru.wikipedia.org/wiki/Параллельные_вычисления",
    "https://habr.com/ru/articles/865974/"
]

if __name__ == '__main__':
    with Pool(3) as pool:
        results = pool.map(fetch_url, urls_habr_wiki)
        for result in results:
            print(result)
            
    with ThreadPool(3) as pool:
        results = pool.map_async(
            fetch_url, 
            urls_habr_wiki, 
            callback=lambda sizes: print("Размеры загруженных страниц:", sizes)
        )
        results.wait()  # Ожидание завершения всех задач