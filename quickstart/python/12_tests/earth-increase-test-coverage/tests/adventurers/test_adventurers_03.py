import pytest
from earth import (
    Adventurer,
    new_panda,
    new_bear,
    Months,
    Busy,
    AirportProblem
)

@pytest.fixture(name="alice")
def fixture_alice():
    return Adventurer(name="Alice", location="Australia", profile="🐨")

# Тестирование создания экземпляров Adventurer
def test_adventurer_creation(alice):
    # adventurer = Adventurer(name="Alice", location="Australia", profile="🐨")
    assert alice.name == "Alice"
    assert alice.location == "Australia"
    assert alice.profile == "🐨"
    assert alice._availability == list(Months)

# Тестирование метода hello
def test_hello_method(capfd):
    adventurer = Adventurer(name="Bob", location="Africa", profile="🦁")
    adventurer.hello()
    captured = capfd.readouterr()
    assert captured.out.strip() == "🦁 Bob Hello, my name is Bob!"

# Тестирование RSVP метода
def test_rsvp_available():
    event = type('Event', (object,), {'month': Months.JUN, 'location': 'Asia'})()
    adventurer = new_bear("Chris")
    
    # Проверяем, что RSVP проходит успешно
    adventurer.rsvp(event)
    assert not adventurer._calendar[Months.JUN]

def test_rsvp_busy():
    event = type('Event', (object,), {'month': Months.JAN, 'location': 'Asia'})()
    adventurer = new_bear("Chris")
    
    # Изменяем доступность на занятость
    adventurer.rsvp(event)
    
    with pytest.raises(Busy):
        adventurer.rsvp(event)

# Тестирование get_ready метода
def test_get_ready(capfd):
    adventurer = Adventurer(name="Diana", location="North America", profile="🐻")
    
    # Проверяем, что get_ready возвращает True после выполнения действий
    is_ready = adventurer.get_ready()
    assert is_ready is True
    
    # Проверяем вывод при подготовке
    captured = capfd.readouterr()
    assert "🐻 Diana is packing" in captured.out

# Тестирование travel_to метода без проблем с аэропортом
def test_travel_to_success(capfd):
    event = type('Event', (object,), {'month': Months.JUN, 'location': 'Asia'})()
    
    adventurer = new_panda("Po")
    
    # Проверяем, что путешествие происходит успешно
    adventurer.travel_to(event)
    
    captured = capfd.readouterr()
    
    assert "🐼 Po is travelling: Asia ✈️  Asia" in captured.out

# Тестирование travel_to метода с проблемами в аэропорту
def test_travel_to_airport_problem(capfd):
    event = type('Event', (object,), {'month': Months.JUN, 'location': 'Unknown'})()
    
    # Создаем приключенца с проблемой в аэропорту
    class MockAirportProblem(AirportProblem):
        pass
    
    def mock_fly(location_from, location_to):
        raise MockAirportProblem("Flight cancelled")
    
    global fly  # Переопределяем функцию fly для теста
    original_fly = fly  # Сохраняем оригинальную функцию fly
    try:
        fly = mock_fly  # Переопределяем на мок-функцию
        
        adventurer = new_panda("Po")
        
        # Проверяем, что происходит обработка проблемы с аэропортом
        adventurer.travel_to(event)
        
        captured = capfd.readouterr()
        assert "🐼 Po's flight was cancelled 😞 Flight cancelled" in captured.out
        
    finally:
        fly = original_fly  # Возвращаем оригинальную функцию fly

