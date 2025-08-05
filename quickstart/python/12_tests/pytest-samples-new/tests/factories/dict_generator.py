from functools import partial #  частично примененная функция может быть вызвана без первого аргумента
from typing import Any, Dict, Union

from factory import Factory
# StubObject - используется для создания "заполненных" объектов, 
# которые могут быть использованы вместо реальных объектов в тестах
# Альтернатива - MockObject, реальзовать 1 из функций объекта
#
# FactoryMetaClass = метакласс, который используется в библиотеке factory_boy
# для определения поведения фабрик
from factory.base import StubObject, FactoryMetaClass


# from https://github.com/FactoryBoy/factory_boy/issues/68#issuecomment-636452903
def generate_dict_factory(the_factory: Union[StubObject, FactoryMetaClass]):
    """Использование:
    DictFactory = generate_dict_factory(MyFactory)
    my_dict = DictFactory()
    """
    def convert_dict_from_stub(stub: StubObject) -> Dict[str, Any]:
        stub_dict = stub.__dict__
        for key, value in stub_dict.items():
            if isinstance(value, StubObject):
                stub_dict[key] = convert_dict_from_stub(value)
        return stub_dict

    def dict_factory(stub_factory, **kwargs):
        stub = stub_factory.stub(**kwargs)
        stub_dict = convert_dict_from_stub(stub)
        return stub_dict

    return partial(dict_factory, the_factory)
