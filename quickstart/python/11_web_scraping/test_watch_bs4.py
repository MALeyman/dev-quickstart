from bs4 import BeautifulSoup
import requests

# Задаем URL-адрес веб-страницы для парсинга
URL = 'http://parsinger.ru/html/index1_page_3.html'

# Отправляем GET-запрос к указанной странице
response = requests.get(url=URL)

# Устанавливаем кодировку ответа сервера в UTF-8 для корректного отображения текста на кириллице
response.encoding = 'utf-8'

# Преобразуем текст ответа сервера в объект BeautifulSoup с использованием парсера 'lxml'
soup = BeautifulSoup(response.text, 'lxml')

# Ищем блок пагинации (элемент <div> с классом 'pagen') на странице, 
# затем извлекаем из него все вложенные ссылки (элементы <a>)
pagen = soup.find('div', class_='pagen').find_all('a')

# Выводим на экран список найденных ссылок
print(pagen)