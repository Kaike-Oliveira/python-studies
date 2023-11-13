# Log - Abstract

class Log:
    def log(self, message):
        raise NotImplementedError('Add a log message!')


class LogFileMixin(Log):
    def log(self, message):
        print(message)


if __name__ == '__main__':
    l = LogFileMixin()
    l.log('Any thing')
