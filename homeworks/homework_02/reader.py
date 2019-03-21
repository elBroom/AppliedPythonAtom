"""
Модуль работает с файлом и кодировками
Обязанность модуля открыть файл в нужной кодировке и считать данные в виде строки
В случае не корректности кодировки выбрасывает ValueError
В случае ошибки в файловой системе IOError, ошибка поднимается из open
"""


def read_data(filename):
    for coding in ('utf8', 'cp1251', 'utf16'):
        try:
            # Файл открывается максимум 3 раза
            with open(filename, encoding=coding) as f:
                return f.read().strip()
        except UnicodeDecodeError:
            # Пробуем открыть в другой кодировке
            continue
    # Не смогли корректно открыть файл
    raise ValueError
