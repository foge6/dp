from selenium import webdriver
import sys
import codecs
from bs4 import BeautifulSoup

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

def get_page_content(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Запуск браузера в фоновом режиме
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options=options)
    driver.get(url)

    # Ждем загрузки страницы
    driver.implicitly_wait(10)

    # Получаем содержимое страницы
    content = driver.page_source

    soup = BeautifulSoup(content, 'html.parser')
    span_element = soup.find('div', class_='like_views like_views--inActionPanel')
    title = (span_element.get('title').split(' '))
    # Закрываем браузер
    driver.quit()

    return title

url = 'https://vk.com/wall240305905_2963'
content = get_page_content(url)
print(int(content[0])+10)