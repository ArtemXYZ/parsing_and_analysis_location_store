import requests
import pandas as pd


# Устанавливаем адрес запроса
def decode_address(address):
    url = f"https://nominatim.openstreetmap.org/search?format=json&q={address}"
    response = requests.get(url)  # Делаем GET запрос к API Nominatim
    if response.status_code == 200:  # Проверяем статус код
        data = response.json()  # Извлекаем координаты из ответа
        if data:
            latitude = str(data[0]['lat'])  # Преобразование широты в строку
            longitude = str(data[0]['lon'])  # Преобразование долготы в строку
            return latitude, longitude
    return '0', '0'


def insert_lat_lon(any_df: pd.DataFrame) -> pd.DataFrame:
    # ______________________________________________________________________________
    # Добавляем новые столбцы 'lat' и 'lon' со значениями по умолчанию 0
    # Добавляет колонку с номером 1, с именем 'lat', значения для строк столбца = 0
    any_df.insert(1, 'lat', '0')  # Присвоение строковых значений 0 для 'lat'
    any_df.insert(2, 'lon', '0')  # Присвоение строковых значений 0 для 'lon'
    # ______________________________________________________________________________
    for i, address in enumerate(any_df.iloc[:, 0], 0):  # Используем enumerate для получения индекса и значения
        a = decode_address(address)
        if a:
            any_df.at[i, 'lat'] = a[0]  # Начинает работу с нулевой строки по калонке lat
            any_df.at[i, 'lon'] = a[1]
            print(f' {i} Адрес декодирован. Координаты: {a[0]} {a[1]}')  # {any_df.at[i, 'lat']}
    return any_df, print(f'Конец работы декодера!')
