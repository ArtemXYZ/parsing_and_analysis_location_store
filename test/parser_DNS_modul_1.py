import pandas as pd
import requests
from bs4 import BeautifulSoup
from joblib import dump  # модуль сохранения и вызва фреймов данных из другого файла
from joblib import load  # модуль сохранения и вызва фреймов данных из другого файла

# from openpyxl import Workbook
# pip install pandas openpyxl xlsxwriter xlrd
# from pandas.io.excel import ExcelWriter
# import pandas.io.excel.xlsx.writer

URL = "https://bitovayatehnika.ru/magaziny/mvideo"
page = requests.get(URL)  # При помощи requests.get мы совершаем запрос к веб страничке.
soup = BeautifulSoup(page.content, "html.parser")  # Сама функция возвращает ответ от сервера (200, 404 и т.д.),
# а page.content предоставляет нам полный код загруженной страницы

# soup = BeautifulSoup(page, "lxml") lxml - более шустрый парсер.


# print(page) # Если ответ <Response [200]>, то ок.
# print(page.content)

# А дальше идёт тот самый будущий суп из html, который нам и нужно будет разобрать.
# В следующей строке и вступает в игру BeautifulSoup, куда мы передаём первым аргументом весь код страницы,
# а вторым указываем, что это анализировать будем именно html.
# print(soup) - Выведет копию кода страницы.

# print(results.text.strip())  # Так результат станет несколько приятнее для чтения.


results = soup.find("div", {"class": "row", "style": "background:#f9f9f9;padding:20px;"}).find_all("a")
# Работает урааааааа!!!!!сука как я выебался,чтоб найти тебя ебучее решение.
# Данная конструкция позволяет делать более точный поиск (жесткие условия), т.к. иногда find_all выдает все подряд.


# list_city_dns: list[str] = []  # Создаем пустой список, в него поместим результат работы цикла (получим список городов) /
# # и в последующем передадим его в DataFrame.
# for i in results:  # Создаем цикл (перебирает кашу из городов)
#     results_text = i.text  # Создаем переменную results_text и помещаем в нее результат работы цикла, вызывая метод /
#     # text, который удаляет теги и оставляет только собственно сам текст.
#     list_city_dns.append(results_text)  # добавляем в наш список результат работы цикла.
# # print(list_city_dns)  # Проверяем результат в списке.


list_url_dns: list[str] = []
for b in results:
    results_url = "https://bitovayatehnika.ru" + b.get("href")
    # "https://bitovayatehnika.ru/magaziny/mvideo" + /cities/aksai/mvideo = https://bitovayatehnika.ru/cities/aksai/mvideo
    list_url_dns.append(results_url)
# print(results_url)  # Проверяем результат в списке.


# df_city_dns = pd.DataFrame({'city_name_dns': list_city_dns, 'url': list_url_dns}) # Создаем DataFrame с колонками /
# # и помещаем в него содержимое наших выше полученных списков.
# # print(df_city_dns)  # Проверяем результат


# dump(df_city_dns, 'df_city_dns.joblib')  # Сохранение DataFrame в дамп.
df_city_dns = load('df_city_dns.joblib')  # Загрузка содержимого DataFrame из дампа в переменную.
# print(df_city_dns.head())  # Проверяем результат
# print(df_city_dns['url'].head())
# df_city_dns.info() # выводим общую информацию о таблице

# df_city_dns.to_excel("df_city_dns.xlsx", index = False) # Сохраняем в файл эксель (можно в CSV еще).
# , sheet_name='this_data') https://www.codecamp.ru/blog/export-pandas-dataframe-to-excel/

# Пишем функцию, которая будет осуществлять мультистраничный поиск по данным из датафрейма
# (берет из него ссылку, переходит и забирает данные, далее сохраняет в датафрейм)


parsing_list_adres_dns: list[str] = []  # parsing_list_adres_dns - создаем пустой список,
# # куда в последующем поместим результаты парсинга.
# # def search_to_url_dns (): # Какие параметры передать? Название листа, ...
#


for i in list_url_dns:  # (забираем) ссылки из списка list_url_dns.
    get_url_in_list = requests.get(i)  # перебираем циклом
    soup_adres = BeautifulSoup(get_url_in_list.content, "html.parser")  # Получаем суп из всех страниц
    search_tag_to_url = soup_adres.find_all("h6")  # .text .find_all("a")) - текст сработает, файнт выдает ошибку
    for c in search_tag_to_url:  # Переберем результаты поиска по тегам циклом.
        results_text_adres: object = c.text  # Создаем переменную results_text_adres и помещаем в нее результат
        # работы цикла, вызывая метод text, который удаляет теги и оставляет только собственно сам текст.
        # print(results_text_adres) правильно работает только с таким отступом (показывает все адреса )
        parsing_list_adres_dns.append(results_text_adres)
    # return parsing_list_adres_dns
#
# # print(parsing_list_adres_dns)

# df_adres_city_dns = pd.DataFrame({'adres_dns': parsing_list_adres_dns})


# dump(df_adres_city_dns, 'df_adres_city_dns.joblib')  # Сохранение DataFrame в дамп.
df_adres_city_dns = load('df_adres_city_dns.joblib')  # Загрузка содержимого DataFrame из дампа в переменную.
# print(df_adres_city_dns.head())  # Проверяем результат
# df_adres_city_dns.info()
