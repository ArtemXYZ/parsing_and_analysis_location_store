import time

# def get_damp(any_df: object = None, dir_save: str = 'data/save_damp/', name_damp: str = 'nonane',
#              corp_name_prefix: str = '', separator: str = '_', only_protocol: str = False):
#     """
#     Функция сохранения DataFrame(ов) в damp.
#
#     :param any_df: Любой DataFrame, defaults to None
#     :type any_df: object
#
#     :param dir_save: Любая директория для сохранения файла (указать), defaults to '.data/save_damp/'
#     :type dir_save: str
#
#     :param name_damp: Имя дампа (значение в строке имени файла при сохранении), defaults to 'nonane'
#     :type name_damp: str
#
#     :param corp_name_prefix: Имя корпорации,(значение в строке имени файла при сохранении), defaults to ''
#     :type corp_name_prefix: str
#
#     :param separator: Тип разделителя,(значение в строке имени файла при сохранении), defaults to '_'
#     :type separator: str
#
#     :param only_protocol: Возвращает либопуть к директории либо damp, defaults to False
#     :type only_protocol: bool
#
#     :rtype: object
#     :return: damp or string
#
#     :notes:
#     """
#
#     if any_df is not None:
#         if corp_name_prefix == '':
#             compound_name_fails: str = f'{dir_save}df_damp{separator}{name_damp}.joblib'
#             if only_protocol == False:
#                 save_damp = dump(any_df, compound_name_fails)  # Сохранение DataFrame в дамп. filename.
#             else:
#                 return compound_name_fails
#
#         else:
#             corp_name_prefix != ''
#             compound_name_fails = f'{dir_save}df_damp{separator}{name_damp}{separator}{corp_name_prefix}.joblib'
#             if only_protocol == False:
#                 save_damp = dump(any_df, compound_name_fails)
#             else:
#                 return compound_name_fails
#     else:
#         return None
#     return save_damp or compound_name_fails
#
#     # todo потом добавить  *args ** kwargs
#
#
# def get_load_damp(compound_name_fails: str = None):
#     """
#     Функция загрузки damp(а) в переменную. Предполагается использование DataFrame(ов) в качестве входного типа данных.
#
#     :param compound_name_fails: Любой DataFrame, defaults to None
#     :type compound_name_fails: object
#
#     :rtype: object
#     :return: damp
#
#     :notes:
#
#     """
#     if compound_name_fails is not None:
#         get_damp(ddd, only_protocol=True)
#         load_damp = load(compound_name_fails)  # Загрузка содержимого DataFrame из дампа в переменную.
#
#
#     else:
#         return None
#     return load_damp
# start_city = time.perf_counter()
# finish_city = time.perf_counter()
# print(
#     f'________________________________________________________________________________________________\n'
#     f'Затраченное время на город: {str(round((finish_city - start_city), 2))} сек.\n'
#     f'================================================================================================')

# print(f'''________________________________________________________________________________________________
# Затраченное время на город: {str(round((finish_city - start_city), 2))} сек.
# ================================================================================================''')
i = 'i'
start_multi = time.perf_counter()
finish_multi = time.perf_counter()
time_delt = (finish_multi - start_multi)
s = round((time_delt % 3600), 2)  # секунды
m = time_delt // 60  # минуты
print(
    f'Мульти-страничный поиск адресов для {i} отработал! Затраченное время: {m} мин. {s} сек.')
