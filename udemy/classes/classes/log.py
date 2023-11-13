# Log - Abstract

# Imports
from pathlib import Path

# Define the file path
LOG_FILE = Path(__file__).parent / 'log.txt'


class Log:
    def _log(self, message):
        raise NotImplementedError('Add a log message!')

    def log_error(self, message):
        return self._log(f'Error: {message}')

    def log_success(self, message):
        return self._log(f'Success: {message}')


class LogFileMixin(Log):
    def _log(self, message):
        formatted_message = f'{message} ({self.__class__.__name__})'
        print('Saving...')
        with open(LOG_FILE, 'a') as file:
            file.write(formatted_message)
            file.write('\n')


class LogPrintMixin(Log):
    def _log(self, message):
        print(f'Print: {message}')


if __name__ == '__main__':

    log_print = LogPrintMixin()
    log_print.log_error('Any thing')
    log_print.log_success('Any thing')
    
    log_file = LogFileMixin()
    log_file.log_error('Any thing')
    log_file.log_success('Any thing')
