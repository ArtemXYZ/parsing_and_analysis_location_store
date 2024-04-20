import pandas as pd
import datetime
import os
from pandas import DataFrame

dir_save = 'data/save_damp/'
# any_df: object = None
# name_damp: str = 'nonane'
# corp_name_prefix: str = 'пккп'
# separator: str = '_'
# index_label = 'id'
#
# compound_name_fails: str = f'{dir_save}df_damp{separator}{name_damp}.joblib'  # - путь
#
# fails_name_list: list = [compound_name_fails]
# print(fails_name_list)

# excel_writer='D:\\02_Работа\\03_Работа в Python\\01_Проекты\\parsing_and_analysis_location_store\\data\\save_damp\\protocol.xlsx'
# excel_writer = './data/save_damp/protocol.xlsx'


# excel_writer = './data/save_damp/protocol.xlsx'
# io = './data/save_damp/protocol.xlsx'
# protocol_read: DataFrame = pd.read_excel(io)

# io='/Users/datagy/Desktop/Sales.xlsx'
# engine='openpyxl'


# slx_patch = os.path.dirname(__file__) + r'\data\save_damp\protocol.xlsx'

# slx_patch = './data/save_damp/protocol.xlsx'
# slx_patch = 'D:\\02_Работа\\03_Работа в Python\\01_Проекты\\parsing_and_analysis_location_store\\data\\save_damp\\protocol.xlsx'
# slx_patch = r'D:\02_Работа\03_Работа в Python\01_Проекты\parsing_and_analysis_location_store\data\save_damp\protocol.xlsx'


# data = pd.read_excel(slx_patch)
# print(data)
# , engine='openpyxl'

# **********
# df_py = pd.read_excel('./00_Исход/Таблица платежей.xlsx') - раньше этот вариант работал
# **********


# import openpyxl
# from pathlib import Path

# dir_seve_protocol = pd.read_excel(
#     '../data/save_damp/protocol.xlsx')  # - работает  только   на 1 уровень папок  в2 уровня не тянет- относительная ссылка ( 2 точки на две папки выше)
# #  продумать механику с патлиб (что лучше использовать относительный или абсолютный путь?????)
# # r'D:\02_Работа\03_Работа в Python\01_Проекты\parsing_and_analysis_location_store\data\save_damp\protocol.xlsx') # - работает после переустановки openpyxl


# from os.path import expanduser as ospath

# from openpyxl import Workbook

# wb = Workbook()
# if __name__ == '__main__':
# - точка входа. В программировании без этого программа не работает.
# (показывает принадлежность (либо это модуль запущенный в программе или это сам модуль).
# В пайтон не требуется, но считается "Правилом хорошего тона".
#
#     slx_patch = os.path.dirname(__file__) + r'\data\save_damp\protocol.xlsx'
#     data = pd.read_excel(slx_patch)
# else:
#     print('все гуд')

# data_dir = r'\data\save_damp\protocol.xlsx'
# data_dir.exists()

# slx_patch = os.path.dirname(__file__) + r'\data\save_damp\protocol.xlsx'
#
# # slx_patch = '\data\save_damp\protocol.xlsx'
# data = pd.read_excel(slx_patch)
# print(data)
#
# Path(__file__).parent / "myfilename.xyz"
#
## r' - экранирование слешев
# user_home_directory = ospath("~")
#
# excel_file_path = user_home_directory + "/Path/To/Excel/File/Car Sales.xlsx"
#
# other_path_car_sales_data = pd.read_excel(excel_file_path)


# excel_writer = './data/save_damp/protocol.xlsx'
# protocol_read = pd.read_excel(excel_writer)

# , engine='openpyxl'
# \parsing_and_analysis_location_store\data\save_damp


# print(os.getcwd())
#  показать текущую папку
# a = open(r'D:\02_Работа\03_Работа в Python\01_Проекты\parsing_and_analysis_location_store\protocol.xlsx')
# print(a)


# dir_seve_protocol: str = f'../{dir_save}protocol.xlsx'  # - 2 точки на 2 папки выше
#
# data_dir = f'r'{dir_save_protocol}'
# print(data_dir)
#
#
#
# else:
#         препарируем полный путь
#         data_dir = r'{dir_save_protocol}'
#
#
#         if dir_save_protocol == '..data/save_damp/protocol.xlsx':
rrrr = (t, t, h, t)
for i in rrrr:
    print(i)
