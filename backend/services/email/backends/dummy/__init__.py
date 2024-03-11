from services.email.backends.base import EmailBackendBase


class EmailBackend(EmailBackendBase):
    def send(self, to, message):
        pass
