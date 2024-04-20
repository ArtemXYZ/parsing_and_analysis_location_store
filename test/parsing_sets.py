import requests
from bs4 import BeautifulSoup
from requests import Response


# Парсинг-модуль: получение данных из открытых источников в интернете.
# Данный модуль пока что не универсален. Он работает на поиск по определенным тегам на определенных страницах.
# В Последующем планируется обновление (доработка до универсальности).

def get_soup(url: object = None) -> object:
    """Получаем первичный "суп" из тегов по ссылке с помощью BeautifulSoup4.

      :param url: Начальный адрес веб-страницы для запуска парсинга, defaults to None
      :type url: str
      :raises ValueError: Неверное значение переменной, проверьте тип данных (необходимый тип: str)
      :rtype: object
      :return: Подготовка первичных данных для парсинга филиалов магазинов бытовой техники.

      """

    if url is None:
        return None
    else:
        page: Response = requests.get(url)  # При помощи requests.get мы совершаем запрос к веб страничке.
        soup: BeautifulSoup = BeautifulSoup(page.content, "html.parser")
        # Сама функция возвращает ответ от сервера (200, 404 и т.д.),
        # а page.content предоставляет нам полный код загруженной страницы.
    # Возвращаемое значение: первичный "суп" из тегов.
    return soup


def get_city_name_list(soup: object = None) -> list:
    """Получаем список городов присутствия с помощью парсинга.

    :param soup: Первичный "суп" из тегов веб-страницы для парсинга, defaults to None
    :type soup: object
    :raises ValueError: Неверное значение переменной, проверьте тип данных (необходимый тип: object)
    :rtype: list
    :return: Парсинг филиалов магазинов бытовой техники.

    """
    soup = get_soup()  # получаем "суп" из функции get_soup

    if soup is not None:
        results = soup.find("div", {"class": "row", "style": "background:#f9f9f9;padding:20px;"}).find_all("a")
        # Индивидуальная конструкция для поиска нужной информации на страничке.
        # В других страницах теги устроены по другому.
        # В дальнейшем необходимо переработать функцию для универсального поиска.

        list_city: list[str] = []  # Создаем пустой список, в него поместим результат работы цикла

        # получим список городов из "каши" с помощью переборки значений циклом.
        for i in results:  # Создаем цикл (перебирает кашу из городов)
            results_text = i.text  # Создаем переменную results_text и помещаем в нее результат работы цикла, вызывая
            # метод text, который удаляет теги и оставляет только собственно сам текст.
            list_city.append(results_text)  # добавляем в наш список результат работы цикла.
    else:
        return None

    return list_city


def get_city_url_list(soup=None) -> list:
    """Получаем список url адресов страниц с физическими адресами филиалов в каждом городе с помощью парсинга.

    :param soup: Первичный "суп" из тегов веб-страницы для парсинга, defaults to None
    :type soup: list
    :raises ValueError: Неверное значение переменной, проверьте тип данных (необходимый тип: object)
    :rtype: list
    :return: Парсинг филиалов магазинов бытовой техники.

    """
    soup = get_soup()  # получаем "суп" из функции get_soup

    if soup is not None:
        results = soup.find("div", {"class": "row", "style": "background:#f9f9f9;padding:20px;"}).find_all("a")
        # Индивидуальная конструкция для поиска нужной информации на страничке.
        # В других страницах теги устроены по другому.
        # В дальнейшем необходимо переработать функцию для универсального поиска.

        list_url: list[str] = []  # Создаем пустой список, в него поместим результат работы цикла

        # получим список url из "каши" с помощью переборки значений циклом.
        for b in results:
            results_url = "https://bitovayatehnika.ru" + b.get("href")
            list_url.append(results_url)  # добавляем в наш список результат работы цикла.
    else:
        return None

    return list_url


def get_address_list(any_lists: object = None) -> list:
    """Мульти страничный поиск адресов филиалов магазинов бытовой техники по списку url адресов страниц.

    :param any_lists: Список адресов веб-страниц для запуска парсинга, defaults to None
    :type any_lists: list
    :raises ValueError: Неверное значение переменной, проверьте тип данных (необходимый тип: list)
    :rtype: list
    :return: Парсинг адресов филиалов магазинов бытовой техники.

    """
    import_list_url = get_city_name_list()  # Импортируем значение list_url (список ссылок), \
    # вызвав функцию get_city_name_list.

    if soup is not None:
        list_address: list[str] = []  # parsing_list_address_dns - создаем пустой список,\
        # куда в последующем поместим результаты парсинга.

        for i in import_list_url:  # Забираем ссылки из списка list_url.
            get_url_from_list = requests.get(i)  # Перебираем циклом.
            soup_address = get_soup(get_url_from_list)  # Получаем суп из всех страниц поочередно.
            search_tag_in_url = soup_address.find_all("h6")
            for c in search_tag_in_url:  # Переберем результаты поиска по тегам циклом.
                results_text_address: object = c.text  # Создаем переменную results_text_address \
                # и помещаем в нее результат
                # работы цикла, вызывая метод text, который удаляет теги и оставляет только собственно сам текст.

                list_address.append(results_text_address)  # добавляем в наш список результат работы цикла.
        else:
            return None

        return list_address
