from bs4 import BeautifulSoup

# Пример HTML-строки
html_string = """
<div>
    <p>Первый абзац.</p>
    <p>Второй абзац <span>со вложенным</span> текстом.</p>
</div>
"""

# Создание объекта BeautifulSoup
soup = BeautifulSoup(html_string, 'html.parser')

# Использование .text для извлечения всего текста из div
div_text = soup.find('div').text

print(div_text)