# Eletronic

# Imports
from log import LogPrintMixin


class Eletronic:
    def __init__(self, name) -> None:
        self._name = name
        self._is_on = False

    def turn_on(self):
        if not self._is_on:
            print(f'Turning on {self._name}')
            self._is_on = True

    def turn_off(self):
        if self._is_on:
            print(f'Turning off {self._name}')
            self._is_on = False


class Smartphone(Eletronic, LogPrintMixin):
    def turn_on(self):
        super().turn_on()

        if self._is_on:
            self.log_success('Successfully logged!')
        else:
            self.log_error('Cannot log!')

    def turn_off(self):
        super().turn_off()
