# global\
# project_home_directory  # - сначала объявляем перменную глобальной, после присваиваем ей значение,
# только такой порядок
# if __name__ == '__main__':
# project_home_directory: str = os.getcwd()


# print(project_home_directory)

# print(project_home_directory + '/data/save_damp/protocol.xlsx')

# url = "https://bitovayatehnika.ru/magaziny/mvideo"
#
# soup = get_soup(url)
# city_name_list = get_city_name_list(soup)
# city_url_list = get_city_url_list(soup)
# address_list = get_address_list(city_url_list)
# # print(address_list)
# # print(city_url_list)
# # далее сохраняем набор листов  в датафрейм
#
# # Тест удался!
# ddd = get_df_city(city_name_list, city_url_list, 'v')
# # print(ddd)
#
# # Тест удался!
# # ggg = get_df_address(address_list, 'mv')
# # print(ggg)
# #  corp_name_prefix='mv'
# # todo: переделать в функцию.
#
# # def get_table_excel(city_name_list, get_city_url_list, get_address_list):
# # Функция сохранения DataFrame(ов) в Excel таблицу.
# #  Загрузка / сохранение дампа в Excel таблицу.
#
# # get_damp(ddd)
#
# print(save_damp(ddd, only_protocol=True))
#
# # !!! save_damp = dump(ddd, 'data/save_damp/.joblib') - работает путь без точки. Можно писать, как ф строку
# #
#
#
# # df_city_dns.to_excel("df_city_dns.xlsx", index = False) # Сохраняем в файл эксель (можно в CSV еще).
# # , sheet_name='this_data') https://www.codecamp.ru/blog/export-pandas-dataframe-to-excel/
#
#
# # # df_adres_city_dns = load('df_adres_city_dns.joblib')  # Загрузка содержимого DataFrame из дампа в переменную.
#
#
#
#
#
