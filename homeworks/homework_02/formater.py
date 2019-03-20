import json

def parsing(data):
    if not data:
        raise ValueError

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
        for row in data[1:]:
            if len(row) != count:
                raise ValueError
        return data
    except Exception:
        raise ValueError


def read_json(data):
    try:
        data = json.loads(data)
    except json.decoder.JSONDecodeError:
        raise ValueError

    try:
        result = [list(data[0].keys())]
        for item in data:
            result.append([
                str(item[column_name])
                for column_name in result[0]
            ])
    except (KeyError, IndexError):
        raise IOError
    return result
