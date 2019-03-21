"""
Модуль работает с форматами json и tsv
Обязанность модуля преобразовать строку в массив,
где первая строка это заголовок, а содержимое равно кол-ву столбцов в заголовке
В случае не консистентности данных выбрасывает ValueError

Обратите внимание: модуль не знает откуда берутся данные из файла,
командной строки, базы данных или приходят по сети, он знает что есть строка и ВСЕ
"""

import json


def parsing(data):
    # data - строка
    if not data:
        raise ValueError

    # Отдаем список где первая строка это заголовок
    try:
        return read_json(data)
    except ValueError:
        return read_tsv(data)
    except IOError:
        pass
    raise ValueError


def read_tsv(data):
    try:
        data = [row.split('\t') for row in data.strip().split('\n')]
        count = len(data[0])
        # Проверка на разное кол-во колонок
        for row in data[1:]:
            if len(row) != count:
                raise ValueError
        return data
    except Exception:
        raise ValueError


def read_json(data):
    # Пробуем распарсить данные как json
    try:
        data = json.loads(data)
    except json.decoder.JSONDecodeError:
        raise ValueError

    try:
        # Формируем список, где ключи это заголовок таблицы
        result = [list(data[0].keys())]
        for item in data:
            result.append([
                str(item[column_name])
                for column_name in result[0]
            ])
    # KeyError - ключи не консистентны
    # IndexError - нет данных
    except (KeyError, IndexError):
        raise IOError
    return result
