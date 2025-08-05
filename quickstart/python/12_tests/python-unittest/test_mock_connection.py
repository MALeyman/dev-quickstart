import unittest
from unittest import mock

def some_network_function():
    return "Запрос отработал"

class TestNetworkOperations(unittest.TestCase):
    def setUp(self):
        self.mocked_response = mock.Mock()
        self.mocked_response.json.return_value = {'key': 'value'}
        self.requests_get_patcher = mock.patch('requests.get', return_value=self.mocked_response)
        self.mocked_requests_get = self.requests_get_patcher.start()

    def tearDown(self):
        self.requests_get_patcher.stop()

    def test_network_request(self):
        response = some_network_function()  # Функция, которая делает сетевой запрос
        self.mocked_requests_get.assert_called_once()  # Проверяем, что запрос был сделан
        self.assertEqual(response, {'key': 'value'})  # Проверяем моковые данные