import requests
from bs4 import BeautifulSoup
from joblib import dump  # модуль сохранения и вызова фреймов данных из другого файла
from joblib import load  # модуль сохранения и вызова фреймов данных из другого файла


def get_city_name_list(url=None, corp_name_prefix=None) -> object:
    """Получаем список городов присутствия с помощью парсинга.

    :param url: начальный адрес веб-страницы для запуска парсинга, defaults to None
    :type url: str

    :param corp_name_prefix: в переменную передается имя магазина, оно прописывается в дальнейшем при создании
    переменных и названия колонок в датафрейме, defaults to None
    :type corp_name_prefix: str or int

    :raises ValueError: Неверное значение переменной, проверьте тип данных переменной (необходимый тип: str)
    :rtype: object
    :return: Парсинг адресов филиалов магазинов бытовой техники.
    """

    # :raises <тип ошибки>: <описание ошибки> - описывает ошибки
    # :rtype: <return_ тип >  возвращаемое значение и его тип
    # :return < возвращаемое описание >

    if url == None:
        return url
    else:
        page = requests.get(url)  # При помощи requests.get мы совершаем запрос к веб страничке.
        soup = BeautifulSoup(page.content, "html.parser")
        # Сама функция возвращает ответ от сервера (200, 404 и т.д.),
        # а page.content предоставляет нам полный код загруженной страницы.
        results = soup.find("div", {"class": "row", "style": "background:#f9f9f9;padding:20px;"}).find_all(
            "a")

        list_city: list[str] = []  # Создаем пустой список, в него поместим результат работы цикла

        # (получим список городов) и в последующем передадим его в DataFrame.
        for i in results:  # Создаем цикл (перебирает кашу из городов)
            results_text = i.text  # Создаем переменную results_text и помещаем в нее результат работы цикла, вызывая
            # метод text, который удаляет теги и оставляет только собственно сам текст.
            list_city.append(results_text)  # добавляем в наш список результат работы цикла.

        # (получим список url) и передадим его в DataFrame.
        list_url: list[str] = []
        for b in results:
            results_url = "https://bitovayatehnika.ru" + b.get("href")
            list_url.append(results_url)  # добавляем в наш список результат работы цикла.

        # Создаем DataFrame с колонками и помещаем в него содержимое наших выше полученных списков.
        df_city: DataFrame = pd.DataFrame({f'city_name_{corp_name_prefix}': list_city, 'url': list_url})

    return df_city  # Возвращаем значение DataFrame.

    dump(df_city, f'df_city_{corp_name_prefix}.joblib')  # Сохраненяем DataFrame в дамп.
    df_city = load(f'df_city_{corp_name_prefix}.joblib')  # Загрузка содержимого DataFrame из дампа в переменную.

    # Проверяем есть ли дамп DataFrame в папке проекта.
    return df_city
