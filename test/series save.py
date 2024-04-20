import pandas as pd

dir_save = '.data/save_damp/'
any_df: object = None
name_damp: str = 'nonane'
corp_name_prefix: str = 'пккп'
separator: str = '_'
index_label = 'id'

############# Сохраняем комбинироваанное имя #############
compound_name_fails: str = f'{dir_save}df_damp{separator}{name_damp}.joblib'  # - путь
# print(compound_name_fails)

############# Сохраняем Series - уже не надо ############# Схема рабочая. Путь только так воспринимает.
series_to_excel = pd.Series(compound_name_fails)  # - Работает. Из одной колонки можно только Series создать
############# Сохраняем дата фрем #############


print(series_to_excel)
############# Сохраняем в переменной путь #############
excel_writer = 'D:\\02_Работа\\03_Работа в Python\\01_Проекты\\parsing_and_analysis_location_store\\data\\save_damp\\protocol.xlsx'  # Работает

############# Сохраняем файл эксель, он же протокол #############
series_to_excel.to_excel(excel_writer, sheet_name=corp_name_prefix, index=True, index_label=index_label)
