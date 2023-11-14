# Abstract Base Class

# Imports
from abc import ABC, abstractmethod


class Log(ABC):
    @abstractmethod
    def _log(self, message): ...

    def log_error(self, message):
        return self._log(f'Error: {message}')

    def log_success(self, message):
        return self._log(f'Success: {message}')


class LogPrintMixin(Log):
    def _log(self, message):
        print(f'Print: {message}')


l = LogPrintMixin()
l.log_error('Hello!')
