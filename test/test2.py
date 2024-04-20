from globals import project_home_directory  # - импорт всех переменных (предпочтительнее)
import os

import pandas as pd
import datetime
import openpyxl
from pandas import DataFrame
from pandas.io.excel import ExcelWriter
from globals import *

# path_damp: str = r'\data\save_damp'  # .? на слеш в конце строки ругается, нужен метот джоин + 'protocol.xlsx'
# path_protocol1: str = project_home_directory + path_damp + r'\protocol.xlsx'
# print(path_protocol1)  # D:\02_Работа\03_Работа в Python\01_Проекты\parsing_and_analysis_location_store\data\save_damp\protocol.xlsx
#
# path_protocol2: str = os.path.join(
#     project_home_directory + path_damp + r'\protocol.xlsx')  # = \data\save_damp\protocol.xlsx
# print(path_protocol2)  # D:\02_Работа\03_Работа в Python\01_Проекты\parsing_and_analysis_location_store\data\save_damp\protocol.xlsx
path_save_protocol: str = r'\data\save_damp'

dir_save_protocol = (project_home_directory + path_save_protocol + r'\protocol.xlsx')
corp_name_prefix = 'dns'

# def read_protocol(dir_save_protocol, corp_name_prefix: str):
#     if os.path.isfile(dir_save_protocol) == True:  # Если файл существует,тогда читаем:
#         if corp_name_prefix in book.sheetnames:  # Если существует страница с таким именем:
#             load_df = pd.read_excel(dir_save_protocol, engine="openpyxl", sheet_name=corp_name_prefix,
#                                     index_col=0).set_index('id')
#             print('x')
#             # print(max(load_df['id']))  # sort_values(max
#         else:
#             print(f'Невозможно загрузить дамп: отсутствует лист с именем {corp_name_prefix} в протоколе!')
#     else:
#         return print(f'Невозможно загрузить дамп: отсутствует файл протокола!')
load_df = pd.read_excel(dir_save_protocol, engine="openpyxl", sheet_name=corp_name_prefix)
# index_col=0 не хочет  читать индекс в функции idxmax()
#
# load_path_damp = (load_df['full path to fails'].loc[load_df['id'].idxmax()])  # работает(полная формула)

range_id = load_df['id'].idxmax()  # максимальное значение для id работает (оследняя загрузка)
load_path_damp = (load_df['full path to fails'].loc[range_id])  # работает- эквивалент полной функции
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
    print('Дамп успешно загружен!')

#     load(load_path_damp)
#     break
#     print('нашел')
# else:
#     continue
#     print('Ищем дальше')

# load_path_damp

# for r in range_id:
# load_path_damp = r - 1
# print(r)

# break  — прерывает цикл и выходит из него;
# continue — прерывает текущую итерацию и переходит к следующей.
# full path to fails

# print(load_df['id'].idxmax())  # = 1 работает

# print(load_df.loc[load_df['id'].idxmax()])  # работает но выводит  строки всех колонок в  датафрейме

# print(columns.loc[load_df['id'].idxmax()])  # работает
#
# print(load_df['relative path to fails'].loc[load_df['id'].idxmax()])  # работает \
# показывает конкретную строку в конкретной колонке
# load_df['id'].idxmax()])
# print(load_df.iloc())
# load_df['id'].idxmax()))
# ['relative path to fails']
# ['relative path to fails']
# print(load_df)
# print(load_df.index)

# print(load_df['id'])
# print(load_df.head())

# q = load_df.reset_index(level='id')
# print(q.set_index('id'))

# print(q.head(2))
# load_df.as_index = False
# print(load_df.set_index('id')) - индексу и так присвоено имя ids

# print(load_df.iloc[['relative path to fails'] == load_df['id'].max()])
# df_py_filter = df_py[df_py['Источник платежа'].isin(payment_source_list)]
# set_index('id')
# print(load_df['relative path to fails'].iloc[[max(load_df['id'])]])
# print(max(value(load_df['id'])))
# columns = load_df.loc[2]
# print(columns)
#
# if os.path.isfile(load_path_damp) != False:  # Если файл не существует,тогда:
#     i = range_id
#     while i >= 0:
#         range_id = i - 1
#         print(range_id)
#         continue
#
#         # load(load_path_damp)  # Тогда загружаем работает
#         break
#         print(_id)
