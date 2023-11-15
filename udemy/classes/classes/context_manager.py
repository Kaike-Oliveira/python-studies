# Context Manager

class ManagerOpen:
    def __init__(self, path: str, mode: str) -> None:
        self.path = path
        self.mode = mode
        self._file = None

    def __enter__(self):
        print('Opening file...')
        self._file = open(self.path, self.mode, encoding='utf8')
        return self._file

    def __exit__(self, class_exception, exception_, traceback_):
        print('Closing file...')
        self._file.close()


with ManagerOpen('class_manager.txt', 'w') as file:
    file.write('Line one \n')
    file.write('Line two \n')
    file.write('Line three \n')
    print('With', file)
