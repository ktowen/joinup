from services.sms.backend.base import SMSBackendBase


class SMSBackend(SMSBackendBase):
    client = None

    def __init__(self, *args, **kwargs):
        # TODO: Initialize the Twilio client from the settings
        pass

    def send(self, to, message):
        pass
