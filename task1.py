# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.


def path_parsing(absolute_path: str):
    *abs_path, file = absolute_path.split('\\')
    file_name, extension = file.split('.')
    reconstruct_path: str = ''
    for item in abs_path:
        reconstruct_path = reconstruct_path + item + '/'
    my_tuple = (reconstruct_path, file_name, extension)
    return my_tuple


print(path_parsing('C:\Brother\DrvLangChg\start.exe'))
