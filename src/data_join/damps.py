from joblib import dump  # модуль сохранения и вызова фреймов данных из другого файла
from joblib import load  # модуль сохранения и вызова фреймов данных из другого файла
import pandas as pd
import datetime
import openpyxl
from pandas import DataFrame

from globals import *  # - импорт всех переменных (предпочтительнее)
from pandas.io.excel import ExcelWriter
from src.data_join.protocol import *
from src.user_module.path_joiner import *


def save_damp(path_save_protocol: str = None, path_save_damp: str = None, any_df: object = None, separator: str = '_',
              corp_name_prefix: str = 'Noname', name_damp: str = 'Noname'):
    """
    Функция сохранения DataFrame(ов) в damp.

    :param any_df: Любой DataFrame, defaults to None
    :type any_df: object

    :param path_save_damp: путь сохранения файла (указать)
    :type path_save_damp: str

    # :param name_damp: Имя дампа (значение в строке имени файла при сохранении), defaults to 'nonane'
    # :type name_damp: str

    :param corp_name_prefix: Имя корпорации,(значение в строке имени файла при сохранении), defaults to ''
    :type corp_name_prefix: str

    :param separator: Тип разделителя,(значение в строке имени файла при сохранении), defaults to '_'
    :type separator: str

    :param path_save_protocol: путь сохранения протокола
    :type path_save_protocol: str

    :rtype: object
    :return: damp or string

    :notes:
    """
    # full_path_save_damp = os.path.join(project_home_directory + path_save_protocol)  # Собираем полный путь \
    # до файла (нет имени файла). ля случае автономности функции (вызов независисимо от программы)
    # todo: переписать на относительный путь в протоколе, а чтение переработает в абсолютный
    # двойная запись
    if any_df is not None:
        compound_name_files: str = os.path.join(path_save_damp,
                                                f'damp{separator}{name_damp}{separator}{corp_name_prefix}.joblib')
        # -------------------------------------- Сохраняем DataFrame в дамп --------------------------------------------
        save_damp = dump(any_df, compound_name_files)
        # -------------------------------- Записываем данные о сохранении в протокол -----------------------------------
        save_protocol(compound_name_files, corp_name_prefix, path_save_protocol)  # позиционные аргументы
    else:
        return None
    return compound_name_files

# path to packages path_of_folder, path_for_package
# def load_damp(path_save_protocol: str, corp_name_prefix: str):
#     """
#      Функция загрузки damp(а) в переменную. Предполагается использование DataFrame(ов) в качестве входного типа данных.
#
#      :param path_save_protocol: Путь к протоколу для чтения идентификатора загрузки.
#      :type path_save_protocol: str
#
#      :param corp_name_prefix: Имя корпорации.
#      :type corp_name_prefix: str
#
#      :rtype: object
#      :return: damp
#
#      :notes:
#
#      """
#     # for s in input_list_url:  # Переборка циклом значений словаря
#     read_protocol(path_save_protocol, corp_name_prefix)
#     return

#     else:
#         return None
#     return load_damp

# if load_path_damp is not None:


# Загрузка содержимого DataFrame из дампа в переменную.
# compound_name_fails.to_excel('data/save_damp/protocol.xlsx', index = False, устарело удалить после отладки
# sheet_name='corp_name_prefix') # Сохраняем в файл эксель. устарело удалить после отладки
#    if any_df is not None:
#         if corp_name_prefix == '':
#             compound_name_fails: str = f'{dir_save}df_damp{separator}{name_damp}.joblib'
#             if only_protocol == False:
#                 ############# Сохраняем DataFrame в дамп ################
#                 save_damp = dump(any_df, compound_name_fails)
#                 ############# Записываем данные о сохранении в протокол #############
#
#                 # ****** переписать на полный путь!!!!
#                 dir_seve_protocol: str = f'../{dir_save}protocol.xlsx'  # - 2 точки на 2 папки выше
#                 # ****** переписать через модуль ос!!
#                 save_protocol(compound_name_fails, dir_seve_protocol)
#
#
#
#             else:
#                 return compound_name_fails
#
#         else:
#             corp_name_prefix != ''
#             compound_name_fails = f'{dir_save}df_damp{separator}{name_damp}{separator}{corp_name_prefix}.joblib'
#             if only_protocol == False:
#                 ############# Сохраняем DataFrame в дамп ################
#                 save_damp = dump(any_df, compound_name_fails)
#                 ############# Записываем данные о сохранении в протокол #############
#                 # save_protocol(compound_name_fails, dir_seve_protocol)
#
#                 # ????????????
#
#             else:
#                 return compound_name_fails
#     else:
#         return None
#     return save_damp or compound_name_fails

#
# else:
#             compound_name_fails = os.path.join(path_save_damp, f'damp{separator}{corp_name_prefix}.joblib')
#             # -------------------------------------- Сохраняем DataFrame в дамп ----------------------------------------
#             save_damp = dump(any_df, compound_name_fails)
#             # -------------------------------- Записываем данные о сохранении в протокол -------------------------------
#             save_protocol(compound_name_fails, corp_name_prefix, path_save_protocol)
#             # return compound_name_fails
