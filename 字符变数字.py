def is_number(value):
    return value.replace('.', '', 1).isnumeric()


def clean_data(data):
    a = 0
    for i in data:
        if isinstance(i, list):
            data[a] = clean_data(i)
        else:
            if is_number(i):
                data[a] = eval(i)
        a += 1
    return data


if __name__ == '__main__':
    ls = [['abc', '123', '45.6', 'car', 'Bike', '', ['12', 'sd']], ['12.3', 'ds']]
    print(clean_data(ls))
