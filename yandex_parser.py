from selenium import webdriver
from bs4 import BeautifulSoup

# URL веб-страницы, которую нужно спарсить
url = "https://music.yandex.ru/users/TolstiyKolya/playlists/3"

file_name = "yandex_parser.txt"

# Создаем экземпляр браузера Chromedriver
driver = webdriver.Chrome()
driver.get(url)

# Прокручиваем страницу вниз, пока не загрузятся все треки
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    # Прокручиваем страницу вниз
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Ждем, пока страница загрузится
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Создаем объект BeautifulSoup, используя полученный HTML-код
soup = BeautifulSoup(driver.page_source, "html.parser")

# Находим все треки на странице
tracks = soup.find_all("div", class_="d-track__overflowable-wrapper")

# Открываем файл для записи результатов
with open(file_name, "w", encoding="utf-8") as file:
    # Проходим по каждому треку и извлекаем название и исполнителей
    for index, track in enumerate(tracks, start=1):
        title = track.find("a", class_="d-track__title").text.strip()
        artists = [artist.text.strip() for artist in track.find_all("a", class_="deco-link deco-link_muted")]
        artists_string = ", ".join(artists)
        file.write(f"{index}. {title}/{artists_string}\n")

print(f"Результаты сохранены в файле {file_name}")

driver.quit()
