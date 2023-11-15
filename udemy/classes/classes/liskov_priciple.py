# Liskov Substitution Principle

# Imports
from abc import ABC, abstractmethod

# Abstract class, so is only a model


class Notification(ABC):
    def __init__(self, message) -> None:
        self.message = message

    @abstractmethod
    def send(self) -> bool: ...


# Child of abstract class, with funcionality in methods
class EmailNotification(Notification):
    def send(self) -> bool:
        print(f'Email: sending: {self.message}')
        return True


class MessageNotification(Notification):
    def send(self) -> bool:
        print(f'Message: sending: {self.message}')
        return False


# Polimorfism
def notificate(notification: Notification):
    sended = notification.send()

    if sended:
        print('Sent notification!')
    else:
        print('No sent notification!')


email = EmailNotification('message to email...')
message = MessageNotification('message to sms...')

notificate(email)
notificate(message)
