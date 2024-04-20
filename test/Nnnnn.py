import pandas as pd
import datetime
import openpyxl
from pandas import DataFrame

from globals import *  # - импорт всех переменных (предпочтительнее)
from pandas.io.excel import ExcelWriter
from src.user_module.path_joiner import *
from globals import project_home_directory

project_directory = os.path.join(r'\data', 'save_damp' + '\\')  # Директория сохранения дампа и протокола (по умолчанию)
# Нужен еще слеш в конце, не хватает!! - (+ '\\')
path_save_damp: str = get_path(project_directory, project_home_directory, default_path=True)
path_save_protocol: str = get_path(project_directory, project_home_directory, default_path=True)
# ----------------------------------------------------------------------------------------------------------------------
input_list_url: dict[str, str] = {  # создадим словарь с перечнем url и именами корпораций:
    'dns': 'https://bitovayatehnika.ru/magaziny/dns',
    'mvideo': 'https://bitovayatehnika.ru/magaziny/mvideo',
    'eldorado': 'https://bitovayatehnika.ru/magaziny/eldorado',
    'kcentr': 'https://bitovayatehnika.ru/magaziny/korporaciya-centr',
    'rbt': 'https://bitovayatehnika.ru/magaziny/rbt'
}


def read_protocol(path_save_protocol: str = None, corp_name_prefix: str = '') -> object:
    """
    Функция чтения "идентификатора загрузки" дампа (уникальное имя файла и путь) в протоколе.

    :param dir_seve_protocol: Сохраняемое в протоколе комбинированное имя файла ("идентификатора загрузки"),
    defaults to None
    :type dir_seve_protocol: str

    :param corp_name_prefix: Имя корпорации, будет использовано, как имя листа, defaults to None
    :type corp_name_prefix: str

    :rtype: Object
    :return: compound_name_fails
    :notes:
    """
    path_save_protocol_file = (path_save_protocol + 'protocol.xlsx')  # - Собираем полный путь до файла.
    if os.path.isfile(path_save_protocol_file) == True:  # Если файл существует,тогда читаем:
        if corp_name_prefix in book.sheetnames:  # Если существует страница с таким именем:
            load_df: DataFrame = pd.read_excel(path_save_protocol_file, engine="openpyxl", sheet_name=corp_name_prefix)
            # ---------------------------------------------------------------------------------------------------------
            range_id = load_df['id'].idxmax()  # максимальное значение для id работает (оследняя загрузка)
            load_path_damp = (load_df['full path to fails'].loc[range_id])  # работает - эквивалент полной функции
            #  ---------------------------------------------------------------------------------------------------------
            if os.path.isfile(load_path_damp) == False:  # Если файл не существует,тогда:
                i = range_id
                while i >= 0:
                    range_id = i - 1
                    if os.path.isfile(load_path_damp) == False:
                        continue
                    else:
                        break
                    load(load_path_damp)  # Тогда загружаем работает
                print('Загружен предыдущий дамп в протоколе.')
            else:  # Если удалось найти файл, тогда читаем запись
                # continue
                load(load_path_damp)  # Тогда загружаем работает
                print(f'Дамп {corp_name_prefix} успешно загружен!')
        else:
            print(f'Невозможно загрузить дамп: отсутствует лист с именем {corp_name_prefix} в протоколе!')
    else:
        print(f'Невозможно загрузить дамп: отсутствует файл протокола!')
    return


read_protocol(path_save_protocol, corp_name_prefix='dns')
