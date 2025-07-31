from multiprocessing.pool import Pool
from multiprocessing.pool import ThreadPool # multiprocessing.dummy обертка threading, concurrent
import time

# Асинхронное создание миниатюр изображений
# Имитация длительной операции
# def create_thumbnail(image, num):
#     print(f"Создание миниатюры для {image}...") # библиотека, учебный пример
#     # Имитация времени на обработку изображения
#     time.sleep(2 / num)
#     return f"Миниатюра для {image} создана."

# # Callback-функция для асинхронного вывода результатов
# def on_completion(result):
#     print(result)

# if __name__ == '__main__':
    
#     images = ['image1.jpg', 'image2.jpg', 'image3.jpg']
#     with Pool(4) as pool:
#         results = [
#             pool.apply_async(
#                 create_thumbnail, 
#                 (image, num), callback=on_completion
#             ) for num, image in enumerate(images, start=1)
#             ]

#     # pool.close()
#     # pool.join()

# Асинхронное выполнение вычислений с обратным вызовом
def complex_calculation(x):
    in_start = time.time()
    print(f"Вычисление для {x}...")
    # Имитация сложного вычисления
    calculation = [n ** n for n in range(5_000)]
    return x * x, time.time() - in_start

# Callback-функция для асинхронного вывода результатов
def on_completion(result):
    print(f"Результат вычисления: {result[0]}. Время на задачу: {result[1]:.3f}")
    
if __name__ == '__main__':
    start = time.time()
    with Pool(4) as pool:
    # with ThreadPool(4) as pool:
        numbers = [1, 2, 3, 4]
        for number in numbers:
            pool.apply_async(complex_calculation, (number,), callback=on_completion)
            
    print(f'Время выполнения программы: {time.time() - start:.3f}')
    
    start = time.time()
    
    with ThreadPool(4) as pool:
        numbers = [1, 2, 3, 4]
        for number in numbers:
            pool.apply_async(complex_calculation, (number,), callback=on_completion)
            
    print(f'Время выполнения программы: {time.time() - start:.3f}')
    
