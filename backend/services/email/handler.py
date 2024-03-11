from django.conf import settings
from django.utils.module_loading import import_string


class EmailService:
    backend = None

    def __init__(self):
        backend_class = self.get_backend_class()
        self.backend = backend_class()

    def send(self, to, message):
        self.backend.send(to, message)

    @staticmethod
    def get_backend_class():
        return import_string(settings.EMAIL_SERVICE_BACKEND)
