"""
Модуль работает с отображением
Обязанность модуля вывести содержимое массива на экран
где в массиве первая строка это заголовок, а содержимое равно кол-ву столбцов в заголовке

Обратите внимание: модуль не знает ничего о формате json/tsv или еще что то
"""


def draw(data):
    # Считаем максимальную ширину колонки
    max_sizes = [0 for _ in data[0]]
    for row in data:
        for i, item in enumerate(row):
            max_sizes[i] = max(max_sizes[i], len(item))

    # Рисуем разделитель для строк
    print('-' * (sum(max_sizes) + len(max_sizes) * 5 + 1))
    # Рисуем шапку
    print('|'+'|'.join([
        item.center(max_sizes[i] + 4)
        for i, item in enumerate(data[0])
    ])+'|')
    # Рисуем содержимое
    for row in data[1:]:
        # Последняя колонка по правому краю с отступами в 2 пробела
        # Остальные колонки по левому краю отступами в 2 пробела
        print('|'+'|'.join([
            '  {}  '.format(
                item.rjust(max_sizes[i])
                if i == (len(max_sizes) - 1)  # проверка на последнюю колонку
                else item.ljust(max_sizes[i])
            )
            for i, item in enumerate(row)
        ])+'|')
    # Рисуем разделитель для строк
    print('-' * (sum(max_sizes) + len(max_sizes) * 5 + 1))
