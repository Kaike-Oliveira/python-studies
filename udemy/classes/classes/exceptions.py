# Exceptions

class CustomError(Exception):
    ...


def show_error():
    raise CustomError('Custom error!')


try:
    show_error()
except CustomError as error:
    print(error.args)
