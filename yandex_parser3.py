import requests
from bs4 import BeautifulSoup
import time

# URL веб-страницы, которую нужно спарсить
url = "https://music.yandex.ru/users/TolstiyKolya/playlists/3"

file_name = "yandex_parser.txt"

# Отправляем GET-запрос на веб-страницу
response = requests.get(url)

# Создаем объект BeautifulSoup, используя полученный HTML-код
soup = BeautifulSoup(response.content, "html.parser")

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
