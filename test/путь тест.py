import os
from globals import *

# os.path.join('a', 'b', 'c')


# path_save_protocol: str = r'\data\save_damp'
# name_protocol = 'protocol'
# path_save_protocol = os.path.join(r'\data', 'save_damp', f'{name_protocol}.xlsx')
# print(path_save_protocol)
#
# # dir_save_protocol = (project_home_directory + path_save_protocol + r'\protocol.xlsx')
# dir_save_protocol = os.path.join(project_home_directory + path_save_protocol)
# print(dir_save_protocol)
name_protocol = 'protocol'

path_save_damp: str = os.path.join(project_home_directory + r'\data', 'save_damp')
# print(path_save_damp)

path_save_protocol = os.path.join(project_home_directory + r'\data', 'save_damp', f'{name_protocol}.xlsx')
print(path_save_protocol)
separator = '_'
name_damp = '!'
compound_name_fails: str = os.path.join(path_save_damp, f'df_damp{separator}{name_damp}.joblib')
print(compound_name_fails)
