from services.sms.backends.base import SMSBackendBase


class SMSBackend(SMSBackendBase):
    def send(self, to, message):
        pass
