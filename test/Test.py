# from get_city import get_city_name_list
#
# # from tqdm import tqdm убрать с этим модулем не работает
# # for i in tqdm(range(100)): убрать с этим модулем не работает
#
# url = "https://bitovayatehnika.ru/magaziny/mvideo"
# corp_name_prefix = 'mv'
#
# # print(get_city_name_list(url, corp_name_prefix))
# print(get_city_name_list(url, corp_name_prefix))
#
#
# # get_city_table
#
#     """Сохраняем результат работы BeautifulSoup4 в виде списков в DataFrame.
#
#     :param city_name_list: Список городов, defaults to None
#     :type city_name_list: list
#
#     :param city_url_list: Список url адресов, defaults to None
#     :type city_url_list: list
#
#     :param name_columns_city: Имя столбца с наименованиями городов, defaults to 'city_name'
#     :type name_columns_city: str
#
#     :param name_columns_url: Имя столбца с url адресами, defaults to 'city_name'
#     :type name_columns_url: str
#
#     :param corp_name_prefix: Наименование организации, defaults to ''
#     :type corp_name_prefix: str
#
#     :raises ValueError: Неверное значение переменной, проверьте тип данных (необходимый тип: list).
#     :rtype: Object
#     :return: Подготовка первичных данных для парсинга филиалов магазинов бытовой техники.
#
#     """
# d = "https://bitovayatehnika.ru/magaziny/mvideo"
# a = get_soup(d)
# list_urld = get_city_url_list(a)


# def get_address_list(list_url: list = None) -> Any | None:  # Проверил, функция работает.
#     """Мульти страничный поиск адресов филиалов магазинов бытовой техники по списку url адресов страниц.
#
#     :param list_url: Список адресов веб-страниц для запуска парсинга, defaults to None
#     :type list_url: list
#     :raises ValueError: Неверное значение переменной, проверьте тип данных (необходимый тип: list)
#     :rtype: list
#     :return: Парсинг адресов филиалов магазинов бытовой техники.
#
#     """
#     # import_list_url = get_city_name_list()  # Импортируем значение list_url (список ссылок), \
#     # вызвав функцию get_city_name_list.
#
#     if list_url is not None:
#         list_address: list[str] = []  # parsing_list_address_dns - создаем пустой список,\
#         # куда в последующем поместим результаты парсинга.
#         for i in list_url:  # Забираем ссылки из списка list_url.
#             get_url_from_list: Response = requests.get(i)  # Перебираем циклом.+
#             soup_address = BeautifulSoup(get_url_from_list.content, "html.parser")
#             # Получаем суп из всех страниц поочередно. +
#             # search_tag_in_url = soup_address.find_all("h6")
#             # for c in search_tag_in_url:  # Переберем результаты поиска по тегам циклом.
#             #     results_text_address: object = c.text  # Создаем переменную results_text_address \
#             #     # и помещаем в нее результат
#             #     # работы цикла, вызывая метод text, который удаляет теги и оставляет только собственно сам текст.
#             #
#             #     list_address.append(results_text_address)  # добавляем в наш список результат работы цикла.
#         else:
#             return None
#
#         return list_address

# b = get_city_name_list(a)
# c = get_city_url_list(a)
# # print(c)
# k = get_address_list(c)
# print(k)
# print(get_address_list(list_urld))

# protocol=True

dir_save = '.data/save_damp/'
any_df: object = None
name_damp: str = 'nonane'
corp_name_prefix: str = ''
separator: str = '_'

compound_name_fails: str = f'{dir_save}df_damp{separator}{name_damp}.joblib'
print(compound_name_fails)

if any_df is not None:
    # if only_protocol == False:
    if corp_name_prefix == '':
        compound_name_fails: str = f'{dir_save}df_damp{separator}{name_damp}.joblib'
        if only_protocol == False:
            save_damp = dump(any_df, compound_name_fails)  # Сохранение DataFrame в дамп. filename.

else:
    corp_name_prefix != ''
    compound_name_fails = f'{dir_save}df_damp{separator}{name_damp}{separator}{corp_name_prefix}.joblib'
    save_damp = dump(any_df, compound_name_fails)
else:
return compound_name_fails
else:
return None

return save_damp
