import pytest
from pytest import approx

from source.sut import SystemUnderTest

# @pytest.mark.unit
def test_with_approx():
    """Сравнение приближенных значений pytest.approx"""
    result = SystemUnderTest.function(2)

    assert result == approx(3.99, 4.01), "Результат должен быть равен 4, в пределах допустимого диапазона"


