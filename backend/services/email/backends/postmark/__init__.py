from services.email.backends.base import EmailBackendBase


class EmailBackend(EmailBackendBase):
    client = None

    def __init__(self, *args, **kwargs):
        # TODO: Initialize the Postmark client from the settings
        pass

    def send(self, to, message):
        pass
