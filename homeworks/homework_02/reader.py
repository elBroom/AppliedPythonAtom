def read_data(filename):
    for coding in ('utf8', 'cp1251'):
        try:
            with open(filename, encoding=coding) as f:
                return f.read().strip()
        except UnicodeDecodeError:
            continue
    raise ValueError
