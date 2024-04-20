# Модуль взаимодействия с Юзером:
# print(f'Запущена программа работы с данными о конкурентах ДНС.')
def pars_or_load():
    """
    Функция запускает либо парсинг, либо загрузку предыдущих данных посредством диалога с пользователем.
    :return: input_value.
    :rtype: str
    """
    input_value: str = input(
        f'Желаете обновить данные о конкурентах (запустить парсинг филиалов) или загрузить имеющиеся данные?\n'
        f'Введите: "1" для парсинга, "0" - для загрузки дампа: ')
    while str(input_value) != '1' and str(input_value) != '0':
        input_value: str = input(f'Неправильный ввод команды! Введите "1" или "0": ')
    else:
        print('Команда принята.')
    return input_value

# # new_path = os.path.join(input(f'Введите новую директорию для сохранения файла: '))
# # print(new_path)
# # # D:\00_Видеоклипы
# # path_save_damp): str = None

# path_save = os.path.join(project_home_directory + project_directory)
# print(path_save)
