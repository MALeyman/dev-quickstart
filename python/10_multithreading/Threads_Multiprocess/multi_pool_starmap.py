from multiprocessing import Pool
import math

#Расчет расстояния между парами точек.
# def calculate_distance(point1, point2):
#     return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# if __name__ == "__main__":
#     points_pairs = [((1, 1), (4, 5)), ((2, 3), (5, 6)), ((0, 0), (8, 8))]
#     with Pool(4) as pool:
#         distances = pool.starmap(calculate_distance, points_pairs)
#         print(distances)

# Расчет среднего значения для разных наборов чисел
# def calculate_average(*args):
#     return sum(args) / len(args)

# if __name__ == "__main__":
#     number_sets = [(1, 2, 3), (4, 5, 6, 7), (8, 9)]
#     with Pool(2) as pool:
#         averages = pool.starmap(calculate_average, number_sets)
#         print(averages)

# Параллельное применение функций к данным
# Определим две функции, которые мы хотим выполнить параллельно
def power(*args):
    base, exponent = args
    return base ** exponent


def multiply(x, y):
    return x * y


# Эта функция будет вызывать другие функции с аргументами
def apply_function(*function_args):
    func, args = function_args
    return func(*args)


if __name__ == "__main__":
    # Создаем список задач, где каждая задача - это кортеж из функции и кортежа аргументов
    tasks = [
        (power, (300, 50)), 
        (multiply, (236, 456)), 
        (power, (763, 67))
    ]

    # Используем Pool для параллельного выполнения наших функций
    with Pool(3) as pool:
        # Важно: мы передаем функцию apply_function и список задач tasks в starmap
        results = pool.starmap(apply_function, tasks)
        print(results)