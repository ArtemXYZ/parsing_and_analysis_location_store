# Импорт сторонних библиотек
import pandas as pd

# from pandas import DataFrame

"""
Модуль сохранения данных из открытых источников в интернете в виде листов в DataFrame.
Модуль № 2
"""


#   todo: переписать в полный путь через модуль ос
# Тело модуля
def get_df_city(city_name_list: list = None, city_url_list: list = None, corp_name_prefix: str = '',
                name_columns_city: str = 'city_name', name_columns_url: str = 'url'):
    #            Именованные параметры  (работают)
    # def get_df_city(city_name_list: list, city_url_list: list, corp_name_prefix: str = '',
    #                 name_columns_city: str = 'city_name', name_columns_url: str = 'url'):
    #            Позиционные параметры (работают)
    """
                Сохраняем результат работы BeautifulSoup4 в виде списков городов и url в DataFrame.
                
                :param city_name_list: Список городов, defaults to None
                :type city_name_list: list
                
                :param city_url_list: Список url адресов, defaults to None
                :type city_url_list: list
                
                :param name_columns_city: Имя столбца с наименованиями городов, defaults to 'city_name'
                :type name_columns_city: str
                
                :param name_columns_url: Имя столбца с url адресами, defaults to 'city_name'
                :type name_columns_url: str
                
                :param corp_name_prefix: Наименование организации, defaults to ''
                :type corp_name_prefix: str
                
                :rtype: object
                :return: DataFrame

    """

    # Создаем DataFrame с колонками и помещаем в него содержимое наших выше полученных списков.

    if city_name_list and city_url_list is not None:  # Возможна ошибка в операторе and (проверить).

        df_city = pd.DataFrame({f'{name_columns_city}_{corp_name_prefix}': city_name_list,
                                f'{name_columns_url}_{corp_name_prefix}': city_url_list})
        # Создадим колонку с index-ом
        # df_city.set_index['id'] - не работает.
    else:
        return None

    return df_city


def get_df_address(address_list: list = None, corp_name_prefix: str = '',
                   name_columns_address: str = 'addresses_stores'):
    """
                Сохраняем результат работы BeautifulSoup4 в виде списков адресов в DataFrame.

                :param address_list: Список городов, defaults to None
                :type address_list: list

                :param name_columns_address: Имя столбца с наименованиями городов, defaults to 'addresses_stores'
                :type name_columns_address: str

                :param corp_name_prefix: Наименование организации, defaults to ''
                :type corp_name_prefix: str

                :rtype: object
                :return: DataFrame

    """

    # Создаем DataFrame и помещаем в него содержимое нашего выше полученного списка.

    if address_list is not None:  # Возможна ошибка в операторе and (проверить).
        # Преобразуем все элементы в address_list в строки
        address_list = [str(address) for address in address_list]
        # Преобразуем список address_list в список списков, где каждый элемент является списком с одним значением
        # df_address: DataFrame = pd.DataFrame({f'{name_columns_address}_{corp_name_prefix}': address_list})
        df_address = pd.DataFrame(address_list, columns=[
            f'{name_columns_address}_{corp_name_prefix}'])  # позволяет исправить ошибку (все адреса в строку) не работает!
        # Создадим колонку с index-ом
        # df_address.set_index('id')
        # как вставить новый столбец в качестве первого столбца существующего DataFrame:
        # loc=0 возможно 1?, тк есть индекс
        # добавляем внешний ключ city_id
        # df_address.insert(loc=0, column='city_id', value=значения для строк столбца.
        #  Принимает скаляр, последовательность или массив)
    else:
        return None
    return df_address
