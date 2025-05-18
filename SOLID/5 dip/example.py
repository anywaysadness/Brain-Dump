from abc import ABC, abstractmethod


# Абстракция для сервисов уведомлений
class NotificationService(ABC):
    @abstractmethod
    def send(self, message: str):
        pass


# Конкретная реализация для отправки email
class EmailNotification(NotificationService):
    def send(self, message: str):
        print(f"Отправка email: {message}")


# Конкретная реализация для отправки SMS
class SMSNotification(NotificationService):
    def send(self, message: str):
        print(f"Отправка SMS: {message}")


# Высокоуровневый компонент, зависящий от абстракции
class Notifier:
    def __init__(self, notification_service: NotificationService):
        self.notification_service = notification_service

    def notify(self, message: str):
        self.notification_service.send(message)


# Использование
email_service = EmailNotification()
sms_service = SMSNotification()

notifier_email = Notifier(email_service)
notifier_email.notify("Привет! Это уведомление по email.")

notifier_sms = Notifier(sms_service)
notifier_sms.notify("Привет! Это уведомление по SMS.")