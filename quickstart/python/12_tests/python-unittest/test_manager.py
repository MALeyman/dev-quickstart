import unittest
from database_manager import DatabaseManager


class TestDatabaseManager(unittest.TestCase):
    '''
    setUpModule запускается один раз для модуля.
    setUpClass запускается один раз для класса.
    setUp запускается для каждого тестового метода.
    
    Каждый тестовый метод (test_query и test_update) выполняется.
    
    tearDown запускается после каждого тестового метода.
    tearDownClass запускается после выполнения всех тестовых методов в классе.
    tearDownModule запускается после выполнения всех тестов в модуле.
    '''
    
    def setUpModule():
        # Инициализация модульных ресурсов
        print("setUpModule: Initialize module-level resources")
    
    @classmethod
    def setUpClass(cls):
        # Инициализация классовых ресурсов
        print("setUpClass: Open database connection for tests")

    def setUp(self):
        # Инициализация объекта DatabaseManager перед каждым тестом
        self.db = DatabaseManager()
        self.connection = self.db.connect()

    def test_connect(self):
        # Тестирование подключения к базе данных
        self.assertEqual(self.connection, "Connection established")

    def test_disconnect(self):
        # Тестирование отключения от базы данных
        disconnection = self.db.disconnect()
        self.assertEqual(disconnection, "Connection closed")
        
    def test_query(self):
        # Тестирование запроса к базе данных
        print("test_query: Run database query test")

    def test_update(self):
        # Тестирование обновления в базе данных
        print("test_update: Run database update test")

    def tearDown(self):
        # Очистка после каждого теста
        self.connection = None
        self.db = None
        
    def tearDownModule():
        # Очистка модульных ресурсов
        print("tearDownModule: Clean up module-level resources")
        
    @classmethod
    def tearDownClass(cls):
        # Очистка классовых ресурсов
        print("tearDownClass: Close database connection after tests")

# Запуск тестов, если модуль запущен как главный
if __name__ == '__main__':
    unittest.main()