# main.py
import sys

# Ваши импорты
from reader import read_data
from formater import parsing
from viewer import draw

if __name__ == '__main__':
    filename = sys.argv[1]

    # Ваш код
    try:
        draw(parsing(read_data(filename)))
    except ValueError:
        # Ошибка поднимается из модулей reader, formater
        print('Формат не валиден')
    except IOError:
        # Ошибка поднимается из модуля reader,
        # когда файл не найден или любая другая ошибка ОС при открытии файла
        print('Файл не валиден')
