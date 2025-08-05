import unittest
import sys
from car import Car

class TestCar(unittest.TestCase):
    def setUp(self):
        self.car = Car('Toyota', 'Corolla')
        self.analogCar = Car('toyota', 'corolla')

    def test_init(self):
        '''
        Тест инициализации класса
        '''
        self.assertEqual((self.car.mark, self.car.model), ('Toyota', 'Corolla'), "Неравенство!!!")

    def test_str(self):
        self.assertTrue(str(self.car) == "Марка Toyota Модель Corolla", "Ошибка вывода!!!")

    def test_eq(self):
        self.assertTrue(self.car == self.analogCar, "Ошибка!!!")

    def test_ne(self):
        self.assertFalse(self.car != self.analogCar, "Ошибка!!!")


if __name__ == '__main__':
    # unittest.main()
    stream = sys.stdout
    descriptions=True
    verbosity=2 # verbosity = 2 самый подробный вывод о тесте, verbosity = 0 - ошибки
    
    
    result = unittest.TextTestResult(stream, verbosity, descriptions)
    
    runner = unittest.TextTestRunner(stream=stream, verbosity=verbosity)
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCar)
    runner.run(suite)