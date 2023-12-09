#benchmarking нужен для того чтобы показать как работает функция


def debug_decorator(func):

    def wrapper(*args, **kwargs):
        print(f'Calling func: {func.__name__}')
        print(f'Calling with arguments', args, kwargs)
        result = func(*args, **kwargs)
        print(f'result: {result}')
        return result

    return wrapper


if __name__ == '__main__':
    from src.services import convert_to_currency
    res = convert_to_currency(currency_string='RUB')
