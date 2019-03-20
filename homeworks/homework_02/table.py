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
        print('Формат не валиден')
    except IOError:
        print('Файл не валиден')
