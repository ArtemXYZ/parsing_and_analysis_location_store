import requests
from bs4 import BeautifulSoup
import time
import re

"""
Парсинг-модуль: получение данных из открытых источников в интернете. Данный модуль пока что не универсален. 
Он работает на поиск по определенным тегам на определенных страницах.
В Последующем планируется обновление (доработка до универсальности).
Модуль № 1
"""


def get_soup(url: str = None) -> object:
    """Получаем первичный "суп" из тегов по ссылке с помощью BeautifulSoup4.

      :param url: Начальный адрес веб-страницы для запуска парсинга, defaults to None
      :type url: str
      :raises ValueError: Неверное значение переменной, проверьте тип данных (необходимый тип: str)
      :rtype: object
      :return: Подготовка первичных данных для парсинга филиалов магазинов бытовой техники.

      """

    if url is not None:
        page: Response = requests.get(url)  # При помощи requests.get мы совершаем запрос к веб страничке.
        soup: BeautifulSoup = BeautifulSoup(page.content, "html.parser")
        # Сама функция возвращает ответ от сервера (200, 404 и т.д.),
        # а page.content предоставляет нам полный код загруженной страницы.
        # Возвращаемое значение: первичный "суп" из тегов.
    else:
        return None
    return soup


def get_city_name_list(soup: object = None) -> list[str] | None:  # Проверил, функция работает.
    """Получаем список городов присутствия с помощью парсинга.

    :param soup: Первичный "суп" из тегов веб-страницы для парсинга, defaults to None
    :type soup: object
    :raises ValueError: Неверное значение переменной, проверьте тип данных (необходимый тип: object)
    :rtype: list
    :return: Парсинг филиалов магазинов бытовой техники.

    """
    # soup = get_soup()  # получаем "суп" из функции get_soup

    if soup is not None:
        results = soup.find("div", {"class": "row", "style": "background:#f9f9f9;padding:20px;"}).find_all("div", {
            "class": "col-md-6"})
        # results = soup.find("div", {"class": "row", "style": "text-decoration:underline;"}).find_all("a")
        # Индивидуальная конструкция для поиска нужной информации на страничке. , "a"
        # В других страницах теги устроены по другому.
        # В дальнейшем необходимо переработать функцию для универсального поиска.

        list_city: list[str] = []  # Создаем пустой список, в него поместим результат работы цикла
        for i in results:
            results_text = i.find('a').text

            # получим список городов из "каши" с помощью переборки значений циклом.
            # for i in results:  # Создаем цикл (перебирает кашу из городов)
            #     results_text = i.text  # Создаем переменную results_text и помещаем в нее результат работы цикла, вызывая
            # метод text, который удаляет теги и оставляет только собственно сам текст.
            list_city.append(results_text)  # добавляем в наш список результат работы цикла.
    else:
        return None

    return list_city


def get_city_url_list(soup: object = None) -> list[str] | None:  # Проверил, функция работает.
    """Получаем список url адресов страниц с физическими адресами филиалов в каждом городе с помощью парсинга.

    :param soup: Первичный "суп" из тегов веб-страницы для парсинга, defaults to None
    :type soup: object
    :raises ValueError: Неверное значение переменной, проверьте тип данных (необходимый тип: object)
    :rtype: list
    :return: Парсинг филиалов магазинов бытовой техники.

    """
    # soup = get_soup()  # получаем "суп" из функции get_soup

    if soup is not None:
        results = soup.find("div", {"class": "row", "style": "background:#f9f9f9;padding:20px;"}).find_all("div", {
            "class": "col-md-6"})

        # results = soup.find("div", {"class": "row", "style": "background:#f9f9f9;padding:20px;"}).find_all("div", {
        #     "class": "col-md-6", "style": "text-decoration:underline;"})

        # results = soup.find("div", {"class": "row", "style": "text-decoration:underline;"}).find_all("a")
        # Индивидуальная конструкция для поиска нужной информации на страничке.
        # В других страницах теги устроены по другому.
        # В дальнейшем необходимо переработать функцию для универсального поиска.

        city_url_list: list[str] = []  # Создаем пустой список, в него поместим результат работы цикла
        for b in results:
            results_url = "https://bitovayatehnika.ru" + b.get("href")
            # получим список url из "каши" с помощью переборки значений циклом.
            # for b in results:
            #     results_url = "https://bitovayatehnika.ru" + b.get("href")
            city_url_list.append(results_url)  # добавляем в наш список результат работы цикла.
    else:
        return None

    return city_url_list


def re_delete_fragment_string(address_string: str, fragment: str) -> str:
    '''
    Удаляем слово из строки по шаблону текста.
    Функция на основе регулярки принимает на вход строку и удаляет из нее нужный фрагмент.

    :param address_string: Строка для обрезки. Входные данные.
    :param fragment: Шаблон для извлечения фрагмента из подстроки.
    :return: Обрезанный текст в строке.

    '''
    pattern_to_remove = rf'\{fragment}\b'  # Ищем фрагмент по соответствию шаблона (по границе фрагмента).
    crop_string = re.sub(pattern_to_remove, '', address_string)  # Заменяем фрагмент на ''.
    return crop_string


def delete_by_prefix(address_string: str, corp_name_prefix: str) -> str:
    '''
    Прождолжение функции "delete_by_prefix". Используя ее потенциал происходит проверка по условию для того что бы
    определить соответствующий фрагмент на фход в зависимости от "corp_name_prefix".

    :param address_string: Строка для обрезки. Входные данные.
    :param corp_name_prefix: Имя корпорации.
    :return:
    '''
    if corp_name_prefix == 'dns':
        fragment = 'ДНС'
        string_corp = re_delete_fragment_string(address_string, fragment)
    if corp_name_prefix == 'mvideo':
        fragment = 'МВидео'
        string_corp = re_delete_fragment_string(address_string, fragment)
    if corp_name_prefix == 'eldorado':
        fragment = 'Эльдорадо'
        string_corp = re_delete_fragment_string(address_string, fragment)
    if corp_name_prefix == 'kcentr':
        fragment = 'Корпорация Центр'
        string_corp = re_delete_fragment_string(address_string, fragment)
    if corp_name_prefix == 'rbt':
        fragment = 'RBT'
        string_corp = re_delete_fragment_string(address_string, fragment)
    return string_corp


def get_address_list(city_url_list: list = None, corp_name_prefix: str = None) -> list | None:
    """
    Мульти страничный поиск адресов филиалов магазинов бытовой техники по списку url адресов страниц.
    :param city_url_list: Список адресов веб-страниц для запуска парсинга, defaults to None
    :type city_url_list: list
    :raises ValueError: Неверное значение переменной, проверьте тип данных (необходимый тип: list)
    :rtype: list | None
    :return: Парсинг адресов филиалов магазинов бытовой техники.
    """
    # Добавить корп префикс!!!!
    if city_url_list is not None:  # Забираем ссылки из списка list_url.
        list_address: list[str] = []
        # Получаем суп из всех страниц поочередно, перебирая их циклом.
        # ------------------------------------------------
        for r, i in enumerate(city_url_list, 1):
            start_city = time.perf_counter()  # - время за Город
            # ------------------------------------------------
            start = time.perf_counter()  # - время в секундах
            get_url_from_list: Response = requests.get(i)  # Перебираем циклом.+
            soup_address = BeautifulSoup(get_url_from_list.content, "html.parser")  # Получаем суп из каждой.
            # ------------------------------------------------
            # Получаем: "Имя города" в заголовке (для видимости лога выполнения)!
            search_name_city = soup_address.find("h4").text
            # search_name_city = soup_address.find("div", {"class": "review_card"}).find_all("h4")
            # ------------------------------------------------
            search_tag_in_url = soup_address.find_all("h6")
            finish = time.perf_counter()
            print(
                f'============================================================================================================================================\n'
                f'Получены {search_name_city} за:  {str(round((finish - start), 4))} сек.\n'
                f'____________________________________________________________________________________________________________________________________________')
            # print(f'__Получены еще адреса в за город {search_name_city}. Время работы: ' + str(finish - start))
            # ------------------------------------------------
            start = time.perf_counter()  # -время в секундах
            for b, c in enumerate(search_tag_in_url, 1):  # Переберем результаты поиска по тегам циклом.
                address_string: str = c.text  # Создаем переменную results_text_address \!
                # results_text_address: object = c.text
                results_text_address = delete_by_prefix(address_string, corp_name_prefix)
                # и помещаем в нее результат
                # работы цикла, вызывая метод text, который удаляет теги и оставляет только собственно сам текст.
                # добавляем в наш список результат работы цикла. !
                list_address.append(results_text_address + '\n')
                print(f'       + {b} адрес филиала добавлен: {results_text_address}.')
                # f'       + {b} адрес филиала добавлен: {results_text_address} {str(round((finish - start), 4))} сек.')
                #             Сделать нумерацию
                # ------------------------------------------------ Затраченное время:

            finish_city = time.perf_counter()  # - время за Город
            print(
                f'____________________________________________________________________________________________________________________________________________\n'
                f'Затраченное время на город: {str(round((finish_city - start_city), 2))} сек. Добавлено {b} адрес(ов) \n'
                f'============================================================================================================================================\n'
                f'                                                                    ***                                                                     ')
    else:
        return None
    return list_address, b, r, print(
        f'============================================================================================================================================\n'
        f'Собраны данные о филиалах {corp_name_prefix} в {r} городах. Добавлено {b} адреса(ов) \n'
        f'============================================================================================================================================\n'
        f'                                                                    ***                                                                     ')

# todo: оформить в класс
