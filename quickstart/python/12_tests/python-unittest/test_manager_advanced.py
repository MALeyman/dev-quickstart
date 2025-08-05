import unittest
from database_manager import DatabaseManager

class TestDatabaseOperations(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.db = DatabaseManager()
        cls.db.connect()
        cls.db.create_test_tables()  # Предположим, что этот метод создает тестовые таблицы

    @classmethod
    def tearDownClass(cls):
        cls.db.drop_test_tables()  # Удаляем тестовые таблицы
        cls.db.disconnect()

    def test_data_retrieval(self):
        self.db.insert_test_data()  # Вставляем тестовые данные перед тестом
        data = self.db.retrieve_data()  # Извлекаем данные для теста
        self.assertIsNotNone(data)  # Проверяем, что данные извлекаются
        self.db.clear_test_data()  # Очищаем тестовые данные после теста