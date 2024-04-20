#  перенес все данные в дампс


dir_save = '.data/save_damp/'
any_df: object = None
name_damp: str = 'nonane'
corp_name_prefix: str = 'пккп'
separator: str = '_'

############# Сохраняем комбинированное имя #############
compound_name_fails: str = f'{dir_save}df_damp{separator}{name_damp}.joblib'  # - путь
# print(compound_name_fails)

fails_name_list: list = [compound_name_fails]  # - работает

data_save_protocol: object = datetime.datetime.now()  # - присвоить дату + время сейчас и записать ее
data_save_list: list = [data_save_protocol]

############# Сохраняем дата фрем #############
df_protocol_to_excel = pd.DataFrame({'compound_name_fails': fails_name_list, 'data_save': data_save_list})  # Работает

############# Сохраняем в переменной путь #############
excel_writer = 'D:\\02_Работа\\03_Работа в Python\\01_Проекты\\parsing_and_analysis_location_store\\data\\save_damp\\protocol.xlsx'  # Работает

############# Сохраняем файл эксель, он же протокол #############
df_protocol_to_excel.to_excel(excel_writer, sheet_name=corp_name_prefix, index=True, index_label='id')  # Работает
# Имя листа - Имя корпорации (сделать лди обязательным параметром?
# index=True - Обязательный индекс строки.
# index_label= 'id" - Имя колонки индексов.
# index=True, columns='corp_name_prefix'
# для датафрейма  header = True - показывать имена колонок, по умолчанию тру.


############# Логика выполнения процессов ############# df protocol_reader ():
# Условие:
# Проверяет есть ли в папке (переменная адрес) файл протокол.
# Если нет, то записываем новый.
#
# Если Есть, то читаем файл и ищем записи (протокол сохранения) и на его основе выбираем имя для загрузки дампа.
# Логика записи:
# Исходя из имени дампа (в нем указаны все необходимые индексы для опознавания,
# он же будет частью записи в эксель листе), будет осуществляться опознавание необходимого пути для загрузки.

if read_protocol = pd.read_excel(excel_writer) True and not None:  # импорт объекта таблица "Лицевых счетов" (дата фрем)
# './00_Исход/Таблица ЛС.xlsx'
# выполняем чтение датафрейма по страницам и извлекаем результат
# вставляем в загрузчик.

else:
    return None

################## Мусор

# запись более чем на один лист в рабочей книге:
# pd.ExcelWriter('data/save_damp/protocol.xlsx') as writer:
#     compound_name_fails.to_excel(writer, index=False, sheet_name=corp_name_prefix) , index=True


# df_py_filter = df_py[df_py['Источник платежа'].isin(payment_source_list)] # отфильтровали столбец,
# исключив позиций списания

# ExcelWriter также можно использовать для добавления в существующий файл Excel
#
pd.ExcelWriter('output.xlsx', mode='a') as writer:
#     df1.to_excel(writer, sheet_name='Sheet_name_3')


#
# df1 = pd.DataFrame([['a', 'b'], ['c', 'd']],
#                    index=['row 1', 'row 2'],
#                    columns=['col 1', 'col 2'])
# df1.to_excel("output.xlsx")
