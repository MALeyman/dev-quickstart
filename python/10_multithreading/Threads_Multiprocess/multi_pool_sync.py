from multiprocessing.pool import Pool
from multiprocessing.pool import ThreadPool # multiprocessing.dummy обертка threading, concurrent
import time

# простой пример
# def my_task(n):
#     return n * n

# if __name__ == '__main__':
#     pool = Pool(7)  # Создаем пул из 4 процессов

#     result = pool.apply(my_task, (2,))  # Выполняем функцию my_task с аргументом 2
#     print(result)  # Выводим результат выполнения функции
#     pool.close()

# Синхронное логирование событий
# def log_event(event_id, event_description):
#     # Здесь должен быть код для логирования события в базу данных
#     print(f"Событие {event_id}: {event_description} успешно залогировано.")

# if __name__ == '__main__':
#     with ThreadPool(4) as pool:
#         # Предполагаем, что события генерируются в реальном времени
#         events = [
#             (1, "Система запущена"), 
#             (2, "Пользователь вошел в систему"), 
#             (3, "Данные обновлены")
#         ]

#         for event in events:
#             pool.apply(log_event, event)

#     # pool.close()
#     # pool.join()

# Последовательная обработка файлов

def process_image(image_name):
    # Здесь должен быть код для обработки изображения
    print(f"Обработка {image_name}...")
    time.sleep(5)  # Имитация длительной обработки
    return f"{image_name} обработано."

with ThreadPool(2) as pool:  # Ограничение количества одновременно обрабатываемых изображений
    images = ["image1.jpg", "image2.jpg", "image3.jpg"]

    for image in images:
        result = pool.apply(process_image, (image,))
        print(result)

# pool.close()
# pool.join()