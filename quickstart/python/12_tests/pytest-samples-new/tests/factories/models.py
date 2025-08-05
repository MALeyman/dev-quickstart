from datetime import date

from factory import Faker # генерация подменных данных
from factory.alchemy import SQLAlchemyModelFactory # подменную модель SQLAlchemy
from factory.fuzzy import FuzzyInteger # для генерации случайных целых чисел в определенном диапазоне

from source.models import User # пользователь из программы
from tests import common
from .dict_generator import generate_dict_factory


class UserFactory(SQLAlchemyModelFactory):
    class Meta:
        model = User
        sqlalchemy_session = common.Session
        # указывает, что сессия должна быть сброшена после каждого создания объекта
        sqlalchemy_session_persistence = "flush"  
        # sqlalchemy_get_or_create = ("id",)

    id: int = FuzzyInteger(1, 2147483647)
    first_name: str = Faker("first_name")
    last_name: str = Faker("last_name")
    created_at: float = Faker(
        "unix_time", 
        start_datetime=date(2020, 1, 1), 
        end_datetime=date(2024, 12, 31)
    )


UserDictFactory = generate_dict_factory(UserFactory)
