def draw(data):
    max_sizes = [0 for _ in data[0]]
    for row in data:
        for i, item in enumerate(row):
            max_sizes[i] = max(max_sizes[i], len(item))

    # Это ппц! Но я хочу спать!
    print('-' * (sum(max_sizes) + len(max_sizes) * 5 + 1))
    print('|'+'|'.join([
        item.center(max_sizes[i] + 4)
        for i, item in enumerate(data[0])
    ])+'|')
    for row in data[1:]:
        print('|'+'|'.join([
            '  {}  '.format(item.rjust(max_sizes[i])) if i == (len(max_sizes) - 1) else '  {}  '.format(item.ljust(max_sizes[i]))
            for i, item in enumerate(row)
        ])+'|')
    print('-' * (sum(max_sizes) + len(max_sizes) * 5 + 1))
