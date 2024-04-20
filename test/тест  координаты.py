import requests
import pandas as pd
import re
from joblib import load

address = ' Ижевск, ул. Ворошилова, 53'  # надо удалить 'Корпорация Центр' из адресов


def decode_address(address):
    url = f"https://nominatim.openstreetmap.org/search?format=json&q={address}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data:
            latitude = str(data[0]['lat'])  # Преобразование широты в строку
            longitude = str(data[0]['lon'])  # Преобразование долготы в строку
            return latitude, longitude
    return '0', '0'

    # ______________________________________________________
    # print(decode_address(address))


address_string = 'Корпорация Центр Ижевск, ул. Ворошилова, 53'
fragment = 'Корпорация Центр'


# Функция на основе регулярки.
# Удаляем слово из строки по шаблону текста (регулярное выражение).
def re_delete_fragment_string(address_string: str, fragment: str) -> str:
    '''
    Функция принимает на вход строку и удаляет из нее нужный фрагмент.
    :param address_string: Строка для обрезки.
    :param fragment: Шаблон для извлечения фрагмента из подстроки.
    :return: Обрезанный текст в строке.
    '''
    pattern_to_remove = rf'\{fragment}\b'  # Ищем фрагмент по соответствию шаблона (по границе фрагмента).
    crop_str = re.sub(pattern_to_remove, '', address_string)  # Заменяем фрагмент на ''.
    return crop_str


# ____________________________________________________
# def decode_address(address):
#     url = f"https://nominatim.openstreetmap.org/search?format=json&q={address}"
#     response = requests.get(url)
#     if response.status_code == 200:
#
#         data = response.json()
#         if data:
#             latitude = data[0]['lat']
#             longitude = data[0]['lon']  # Установим тип данных строка
#             return latitude, longitude
#     else:
#         return 0
#     return address
#
#
# def insert_lat_lon(any_df: pd.DataFrame) -> pd.DataFrame:
#     # loc - индекс вставки (номер колонки)
#     # column - Имя вставляемой колонки (индексная метка вставляемого столбца)
#
#     # Добавляем новые столбцы 'lat' и 'lon' со значениями по умолчанию 0
#     any_df.insert(1, 'lat', 0)  # Добавляет колонку с номером 1, с именем 'lat', значения для строк столбца = 0
#     any_df.insert(2, 'lon', 0)
#
#     print(any_df)
#
#     for i, address in enumerate(any_df.iloc[:, 0], 0):
#         a = decode_address(address)
#         if a:
#             any_df.at[i, 'lat'] = str(a[0])  # Установим новое значение для ячейки в строке 'i' и столбце 'lat'
#             any_df.at[i, 'lon'] = str(a[1])
#
#     return any_df

# def insert_lat_lon(any_df: object) -> object:
#     # df = pd.read_csv('cts.csv', delimiter=';', on_bad_lines='skip') заменить загрузкой дампа
#     # df = DataFrame.insert(loc, column, value, allow_duplicates=no_default)
#     # loc - индекс вставки (номер колонки)
#     # column - Имя вставляемой колонки (индексная метка вставляемого столбца)
#     any_df.insert(1, 'lat', 0)  # Добавляет колонку с номером 1, с именем 'lat', значения для строк столбца = 0
#     any_df.insert(1, 'lon', 0)
#     print(any_df)
#     i = 0
#     for i, address in enumerate((any_df.iloc[:, 0]), 0):  # Выбор первого столбца по числовому индексу
#         # 'addresses_stores_kcentr' - имя колонки
#         a = decode_address(address)
#         if a:
#             any_df.at[i, 'lat'] = a[0]  # Установим новое значение для ячейки в строке 'i' и столбце 'lat'
#             any_df.at[i, 'lon'] = a[1]
#             i += 1

#
# (df['lon'] != 0).sum() / df['lon'].count()
# addresses_stores_kcentr


############# Сохраняем в переменной путь ##########
writer = 'D:\\02_Работа\\03_Работа в Python\\01_Проекты\\parsing_and_analysis_location_store\\data\\save_damp\\damp_addres_table_kcentr.joblib'
excel_writer = 'D:\\02_Работа\\03_Работа в Python\\01_Проекты\\parsing_and_analysis_location_store\\data\\save_damp\\damp_addres_table_kcentr.xlsx'
# address_list = ['aasgasga', 'asgaafafh', 'afafdadf', 'afagfgafga']
# df_address = pd.DataFrame(address_list, columns=[f'name_columns_address'])
# print(df_address)
wqr = load(writer)
print(wqr)
df_protocol_to_excel = load(writer)
############# Сохраняем файл эксель, он же протокол #############
df_protocol_to_excel.to_excel(excel_writer)  # Работает
