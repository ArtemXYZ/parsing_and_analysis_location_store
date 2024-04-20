import os
from globals import project_home_directory


def get_path(project_directory: str, project_home_directory: str, default_path: bool = True):
    if default_path is True:
        path_save = os.path.join(project_home_directory + project_directory)
    else:
        new_path: str = os.path.join(
            input(f'Введите новую директорию для сохранения файла: '))  # возможно др. Операторы
        path_save = new_path
    return path_save

#   todo: работа со входящим путем (обрезка нормализация и вывод ошибки в случае несоответствия

# def path_join(any_path: str, name_file: str, extension: str):
#     path_to_file = os.path.join({any_path}, f'{name_file}.{extension}')
#     return path_to_file

# project_directory = os.path.join(r'\data', 'save_damp' + '\\')  # Нужен еще слеш в конце, не хватает!!

# print(get_new_path(project_directory, project_home_directory))
