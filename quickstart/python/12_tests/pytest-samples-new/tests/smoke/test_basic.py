import pytest
from contextlib import contextmanager

from source import SystemUnderTest
# from factory_boy import Factory

'''
Пропущенный тест
'''
@pytest.mark.skip(reason="show skipped")
def test_instantiation():
    SystemUnderTest()

'''
Первый тест на выполнение
'''
@pytest.mark.first
def test_instantiation():
    SystemUnderTest()


def test_simplest():
    # arrange, подготовка
    entry = 23467
    expected = 2*23467
    sut = SystemUnderTest()
    # act, действие
    result = sut.function(entry)
    # assert, проверка соответствия
    assert result == expected


def test_will_fail():
    entry = 1
    expected = 4
    result = SystemUnderTest().function(entry)
    assert result == expected, "Функция должна возвращать двойное значение аргумента или TypeError"


@pytest.mark.xfail(reason="raises an exception", run=True)
def test_with_extra_info():
    # set up, arrange, подготовка
    entry = "1"
    expected = 2
    sut = SystemUnderTest()
    # execution, act, действие
    result = sut.function(entry)
    # assertion, assert, проверка соответствия
    assert result == expected

'''
scope="module" - определяет область видимости фикстуры на уровне модуля
name="sut" - фикстуру "sut" (System Under Test).
'''
@pytest.fixture(scope="module", name="sut")
def system_under_test():
    # set up, arrange, подготовка
    instance = SystemUnderTest()
    yield instance.function
    # tear down, после выполнения
    del instance
    
@pytest.fixture(scope="module", name="sut_manager")
@contextmanager
def system_under_test():
    instance = SystemUnderTest()
    try:
        yield instance.function
    finally:
        # Здесь можно выполнить очистку, если это необходимо
        pass  # или del instance, если действительно нужно удалить

# class SystemUnderTestFactory(Factory):
#     class Meta:
#         model = SystemUnderTest

# @pytest.fixture
# def sut(request):
#     return SystemUnderTestFactory.build()

@pytest.mark.parametrize("entry, expected", (
    (0, 0),
    (1, 2),
    (2, 4),
    ),
    ids=['zero', 'one', 'two']
)
def test_with_params(sut, entry, expected):
    result = sut(entry)
    assert result == expected, "Функция должна возвращать число"


def test_raise():
    with pytest.raises(ValueError) as exc_info:
        SystemUnderTest.raiser(msg="exception msg")

    assert str(exc_info.value) == "exception msg"

