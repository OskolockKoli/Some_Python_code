import requests

# Замените на ваш токен доступа к API Yandex.Music
ACCESS_TOKEN = "y0_AgAAAAAwCT9-AAv1tAAAAAEHs_8dAADLSjs9VvdAbb-KsWIU9Mq28Fu5zw"

# ID плейлиста, который вы хотите получить
PLAYLIST_ID = "3"

# Endpoint для получения информации о плейлисте
endpoint = f"https://api.music.yandex.net/users/TolstiyKolya/playlists/{PLAYLIST_ID}"

# Заголовки для авторизации
headers = {
    "Authorization": f"OAuth {ACCESS_TOKEN}"
}

# Отправляем запрос на получение информации о плейлисте
response = requests.get(endpoint, headers=headers)

# Проверяем, что запрос был успешным
if response.status_code == 200:
    # Получаем данные о плейлисте
    playlist_data = response.json()

    # Проверяем структуру полученных данных
    print(playlist_data)

    if "playlist" in playlist_data:
        # Проходим по каждому треку в плейлисте и записываем информацию
        with open("yandex_parser.txt", "w", encoding="utf-8") as file:
            for index, track in enumerate(, start=1):
                title = track["title"]
                artists = [artist["name"] for artist in track["artists"]]
                artists_string = ", ".join(artists)
                file.write(f"{index}. {title}/{artists_string}\n")

        print("Результаты сохранены в файле yandex_parser.txt")
    else:
        print("Ошибка: в полученных данных нет ключа 'playlist'")
else:
    print(f"Ошибка при получении информации о плейлисте: {response.status_code} - {response.text}")
