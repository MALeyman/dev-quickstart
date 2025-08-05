import unittest
# Главная функция, запускается автоматически

class TestUM(unittest.TestCase):
    # Перегрузка встроенного метода, вызывается перед запуском теста
    def setUp(self):
        print("Запускается перед тестами")
        pass
    # Перегрузка встроенного метода, вызывается после запуском теста
    def tearDown(self):
        print("Запускается после тестов")
        pass
    # Собственные методы
    def check_equal1(self):
        print("выполняем тест1")
        self.assertEqual(14*3, 42)

    def check_equal2(self):
        print("выполняем тест2")
        self.assertEqual('string' * 3, 'stringstringstring')


if __name__ == '__main__':
    unittest.main()