def val_checker(l_funk):
    def _val_checker(funk):
        def wrapper(num):
            if l_funk(num):
                print(funk(num))
            else:
                raise ValueError(f'неверное значение')

        return wrapper

    return _val_checker


@val_checker(lambda x: x > 0)
def calk_cube(x):
    return x ** 3


try:
    a = calk_cube(15)
    b = calk_cube(-47)
except ValueError as error:
    print(error)
