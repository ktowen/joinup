from services.sms.backends.base import SMSBackendBase


class SMSBackend(SMSBackendBase):
    def send(self, to, message):
        print(f"-> SMS sent to {to}: {message}")
