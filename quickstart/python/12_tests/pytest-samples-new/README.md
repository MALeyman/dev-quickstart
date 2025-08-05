# Тестирование с помощью Python

Рассмотрим Тестовый проект для PyConEs 2021 
https://github.com/hectorcanto/pytest-samples?ysclid=m6fen7hree723785178 

Эффективность означает
* Максимально быстрое выполнение тестов
* Разработку и сопровождение кода
* Доступность для всех, особенно для новичков

## Этапы тестирования
Тест может быть разделен на 3 этапа, известные как A (AAA)
* Arrange # организации, кейсы для подготовки, SUT, system under test
* Act # действия, сформировать зависимости
* Assert # проверка результата, который может быть представлен возвращаемым значением, итоговым состоянием тестируемой системы

паттерн «Given-When-Then»
* Given — соответствует секции подготовки (arrange);
* When — соответствует секции действия (act);
* Then — соответствует секции проверки (assert)

## 2 варианта
* с секции подготовки (arrange)
* с секции проверки (assert) TDD

## Настройки командной строки
```cmd
"по папкам"
pytest --help "отображает справочную документацию"
pytest tests/folder/test_file.py::test_name "определенную тестовую функцию в файле"
pytest -m unit "модульные тесты"
pytest -m smoke "быстрые тесты на корректность"
pytest -k users "тесты, имена которых содержат подстроку "users""

"по папкам"
pytest --fail-first "запускает неудачные тесты, а затем остальные тесты"
pytest --last-failed "Выполняет только последние неудачные тесты"
pytest --failed-first "сначала выполняются успешные тесты, а затем неудачные"

pytest -m current -s  -v "помеченные маркером "current""
pytest -m "slow and not integration" "помеченные маркером "slow" и не "integration""
pytest -m "smoke and unit" 
pytest -m "(current and smoke) or unit" 

pytest --markers
````

Тесты в папке [tests/](tests/)
Код для тестов в папке [source/](source/)

Расширенные настройки тестов в папке [tests/confest.py](tests/conftest.py).

## Глоссарий

- fixture: сгенерированный артефакт для использования в тесте, может быть данными, объектом, ...
- factory: функция для создания fixture
- sut: тестируемая система, system under testing
- Smoke-tests — это проверка программного обеспечения на стабильность и наличие явных ошибок. 

## Использование

```bash
pytest
pytest -m unit
```

## Внешняя документация

[Pytest docs](https://docs.pytest.org/)
[Markdown slides for RevealJS](https://github.com/dadoomer/markdown-slides)

#### Примеры тестов
- [Smoke tests](tests/smoke/)
- [Unit tests](tests/unit/)
  - delayed assert: sometimes is useful to run several tests over the same execution,
    but we still want to see them as separated ones
  - отложенное подтверждение (delayed assert): иногда полезно запускать несколько тестов  
    одновременно, но мы все равно хотим, чтобы они были разделены

## Рекомендуемые плагины и библиотеки

Настоятельно рекомендуется:

- Faker: генератор поддельных данных для тестирования (faker)
-- Factory Boy и Polifactory: библиотеки для создания фабрик объектов (factory-boy, polifactory)
- Freezegun - позволяет замораживать время в тестах, использовать с осторожностью (freezegun)
- pytest-xdist: распараллеливание тестов с помощью multiprocessing
- pylint - статический анализатор кода
- flake8 - комбинация PEP 8 и Pyflakes для проверки стиля кода
- любая временная библиотека, такая как timeago, arrow, pendulum ...

- Timeago: это относительно новая библиотека, которая предоставляет удобный способ работы с временными интервалами.
- Arrow: это мощная библиотека для работы с датами и временем, созданная Google.
- Pendulum: это еще одна популярная библиотека для работы с датами и временем.
