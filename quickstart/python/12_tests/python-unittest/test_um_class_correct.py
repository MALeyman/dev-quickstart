import unittest


class TestUM(unittest.TestCase):

    def testAssertTrue(self):
        """
        Проверям истенно ли выражение, иначе исключение
        """

        self.assertTrue(['1' in '0123456789'])

    def testFailUnless(self):
        """
        Устаревшее метод аналогичный testAssertTrue
        """
        self.assertTrue(['1' in '0123456789'])

    def testAssertFalse(self):
        """
        Проверяет ложно ли выражение, иначе исключение
        """
        self.assertTrue(['0' in '123456789'])

    def testFailIf(self):
        """
        Устаревший метод, аналогичег testAssertFalse
        """
        self.assertTrue(['0' in '123456789'])


    def testEqual(self):
        """
        Если 2 переданных параметра не равны, то исключение
        """
        self.failUnlessEqual(15, 13 + 2)

    def testNotEqual(self):
        """
        Если 2 переданных параметра равны, то исключчение
        """
        self.failIfEqual(15, 13 + 3)

    def testEqualFail(self):
        """
        Исключение, если 2 параметра равны
        """
        self.failIfEqual(100, 200)

    def testNotEqualFail(self):
        """
        Исключение, если 2 параметра не равны
        """
        self.failUnlessEqual(1000, 500+500)



if __name__ == '__main__':
    unittest.main()