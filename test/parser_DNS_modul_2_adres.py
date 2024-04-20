import pandas as pd
import requests
from bs4 import BeautifulSoup
from joblib import dump  # модуль сохранения и вызва фреймов данных из другого файла
from joblib import load  # модуль сохранения и вызва фреймов данных из другого файла

# def search_to_url_dns ():
parsing_list_adres_dns: list[str] = []  # parsing_list_adres_dns - создаем пустой список,
# куда в последующем поместим результаты парсинга.

for i in list_city_dns:
    search_to_url = soup_adres.BeautifulSoup((get_url_in_list.requests.get(i.list_city_dns)).content, "html.parser")
    # results_search_to_url = soup_adres.find("div", {"class": "row", "style": "text-decoration:underline;"}).find_all("a")

    # for i in results_search_to_url:  # Создаем цикл
    # results_text_adres: object = i.text  # Создаем переменную results_text и помещаем в нее результат работы цикла, вызывая метод /
    # # text, который удаляет теги и оставляет только собственно сам текст.
    # parsing_list_adres_dns.append(results_text_adres)
    # parsing_list_adres_dns.append(results_search_to_url)
    # df_city_dns = pd.DataFrame({'adres_dns': parsing_list_adres_dns})
