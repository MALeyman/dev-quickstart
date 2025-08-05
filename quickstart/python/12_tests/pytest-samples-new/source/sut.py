from typing import Union

Numeric = Union[int, float]

class SystemUnderTest:
    def __init__(self):
        pass

    @staticmethod
    def function(value: Numeric|None) -> Numeric|None:
        """Функция, возвращающая числовое значение
        Возвращается:
            int или float в зависимости от входных данных, None если None

        Исключения:
            TypeError, если неожиданный тип
        """
        if value is None:
            return None
        if not isinstance(value, (int, float)):
            raise TypeError("Ожидается работа с числом!")
        return 2 * value

    @classmethod
    def raiser(cls, exc=ValueError, msg="Вызвано исключение"):
        raise exc(msg)
