import pandas as pd
import datetime
import openpyxl
from pandas import DataFrame

from globals import *  # - импорт всех переменных (предпочтительнее)
from pandas.io.excel import ExcelWriter

path_protocol: str = r'\data\save_damp\protocol.xlsx'

input_list_url: dict[str, str] = {
    'dns': 'https://bitovayatehnika.ru/magaziny/dns',
    'mvideo': 'https://bitovayatehnika.ru/magaziny/mvideo',
    'eldorado': 'https://bitovayatehnika.ru/magaziny/eldorado',
    'kcentr': 'https://bitovayatehnika.ru/magaziny/korporaciya-centr',
    'rbt': 'https://bitovayatehnika.ru/magaziny/rbt'
}

for i in input_list_url:
    # 0. Подготовка данных:
    # -----------------------------------------Сохраняем в переменной полный путь --------------------------------------
    dir_save_protocol = (project_home_directory + path_protocol)  # - Собираем полный путь до файла.
    #  dir_save_protocol = содержит полный путь (по умолчанию папка сохранения дампа).
    # 1. Проверка существования файла: Если нет (False), то пишем
    not_none_protocol = os.path.isfile(dir_save_protocol)
    # if not_none_protocol is not True:  # Если файла нет.
    # 2. Сохраняем в файл эксель протокол.
    # -------------------------------------- Записываем данные о сохранении в протокол ---------------------------------
    relative_path_to_fails: list = [path_protocol]

    compound_name_fails = dir_save_protocol
    fails_name_list: list = [compound_name_fails]  # Помещаем в лист нашу будущую запись-идентификатор \
    # для протокола (сохранения/загрузки).
    data_save_protocol: object = datetime.datetime.now()  # - Присваиваем дату + время сейчас \
    # и записываем ее в переменную,
    data_save_list: list = [data_save_protocol]  # Помещаем в лист переменную с записью даты.
    # ---------------------------------------- Сохраняем данные в дата фрем --------------------------------------------
    df_protocol_to_excel: DataFrame = pd.DataFrame(
        {'relative path to fails': path_protocol, 'full path to fails': fails_name_list,
         'data_save': data_save_list})
    # ---------------------------------------- Сохраняем файл эксель, он же протокол -----------------------------------
    # for i in corp_name_prefix:
    #     i = corp_name

    # df_protocol_to_excel.to_excel(dir_save_protocol, sheet_name=corp_name_prefix, index=True,
    #                               index_label='id') - +++

    # with ExcelWriter(dir_save_protocol, engine="openpyxl",  # - работает, но не перезаписывает листы
    #                  mode="a" if os.path.isfile(dir_save_protocol) else "w") as writer:
    #     df_protocol_to_excel.to_excel(writer, sheet_name=i, index=True, index_label='id')

    if os.path.isfile(dir_save_protocol) == True:  # Если файл существует,тогда:
        book = openpyxl.load_workbook(dir_save_protocol)
        if i in book.sheetnames:  # Если существует страница:
            # if pd.read_excel(dir_save_protocol, engine="openpyxl", sheet_name=i) == True: # с этим методом надо\
            # использовать try/except:
            # тогда читаем ее и записываем объединенный датафрейм (делаем перезапись листа)
            df_old = pd.read_excel(dir_save_protocol, engine="openpyxl", sheet_name=i, index_col=0)
            concat = pd.concat([df_old, df_protocol_to_excel], axis=0,
                               ignore_index=True)  # соединение датафреймов вертикально
            with (ExcelWriter(dir_save_protocol, engine="openpyxl", mode="a", if_sheet_exists="replace") as writer):
                concat.to_excel(writer, sheet_name=i, index=True, index_label='id')
        else:  # Если не существует страницы:
            with (ExcelWriter(dir_save_protocol, engine="openpyxl", mode="a") as writer):
                df_protocol_to_excel.to_excel(writer, sheet_name=i, index=True, index_label='id')
    else:  # Если файла не существует,тогда:
        with (ExcelWriter(dir_save_protocol, engine="openpyxl", mode="w") as writer):
            df_protocol_to_excel.to_excel(writer, sheet_name=i, index=True, index_label='id')
#
# if_sheet_exists="new"

# if_sheet_exists=  overlay - наложение
# ValueError: Sheet 'noname' already exists and if_sheet_exists is set to 'error'.
# ValueError: Лист "без имени" уже существует, а if_sheet_exists имеет значение "ошибка".
# with ExcelWriter(dir_save_protocol, mode="a") as writer:
#     # mode="w" - записать (файла еще нет)
#     # mode="a" - дописать (файла есть)
#     for i in corp_name_prefix:
#         df_protocol_to_excel.to_excel(writer, sheet_name=i, index=True, index_label='id')
#     mode="w"

#
# else:
#      for i in corp_name_prefix:
#         protocol_read = pd.read_excel(dir_save_protocol)  # пустой ли файл проверка
#         if protocol_read is None:
#             df_protocol_to_excel.to_excel(dir_save_protocol, mode="w", sheet_name=i, index=True,
#                                           index_label='id')  # - просто пишем файл
#
#             with ExcelWriter(dir_save_protocol, mode="a" if os.path.isfile(dir_save_protocol) else "w") as writer:
#                 df_protocol_to_excel.to_excel(writer, sheet_name=i, index=True, index_label='id')
#
#
#
#
#     # df_protocol_to_excel.to_excel(dir_save_protocol, mode="a", sheet_name=corp_name_prefix, index=True,
#     #                               index_label='id')
#     None
# df_protocol_to_excel.to_excel(dir_save_protocol, mode="w", sheet_name=i, index=True,
#                                           index_label='id')  # - просто пишем файл
