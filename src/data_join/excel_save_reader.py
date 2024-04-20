import pandas as pd
import os
# import globals

from globals import *  # - импорт всех переменных (предпочтительнее)
from pandas.io.excel import ExcelWriter

compound_name_fails = ['\data\save_damp\protocol.xlsx']
df = pd.compound_name_fails
# from globals import project_home_directory  # - импорт  одной переменной (глобальной
# import globals - не вытаскивает переменную

# def read_excel(dir_seve_protocol: str = '.data/save_damp/protocol.xlsx'):
#     """
#     Функция чтения протокола в файле эксель.
#
#     :param
#     :type
#
#
#     :rtype:
#     :return:
#
#     :notes:
#     """
#
#     protocol_read = pd.read_excel(dir_seve_protocol)
#
#     if protocol_read == None:
#         a = print(хуй)
#     else:
#         a = print(заебок)
#     return a
#
#
# read_excel()

# D:\\02_Работа\\03_Работа в Python\\01_Проекты\\parsing_and_analysis_location_store\\data\\save_damp\\protocol.xlsx

# engine='openpyxl' - движок. OpenPyXL поддерживает новые форматы MS Excel (.xlsx)
#
#         a: bool = False
#     else:
#         a: bool = True
#     return a

# , engine='openpyxl'


# dir_save_protocol: str = '../data/save_damp/protocol.xlsx'
# protocol_read = pd.read_excel(dir_save_protocol)
# ------------------------------------------------------------------------------------------------------------------
corp_name_prefix: list = ['a', 'b', 'c']
for i in corp_name_prefix:
    print(i)
#

path_protocol = r'\data\save_damp\protocol.xlsx'
dir_save_protocol = (project_home_directory + path_protocol)
# read = pd.read_excel(protocol_read)
# print(read)

for i in corp_name_prefix:
    with ExcelWriter(dir_save_protocol, mode="a") as writer:
        df.to_excel(writer, sheet_name=i, index=True, index_label='id')
# ------------------------------------------------------------------------------------------------------------------
# print(project_home_directory)
# protocol_read = pd.read_excel(

# print(project_home_directory + '/data/save_damp/protocol.xlsx')

# print(os.path.join(project_home_directory, )
# print(protocol_read)

# dir_save_protocol = os.path.dirname(os.path.abspath(__file__))
# protocol_read = pd.read_excel(os.path.join(os.pardir(dir_save_protocol), "protocol.xlsx"))
