from core.celery import app

from users.models import User


@app.task(
    bind=True,
    autoretry_for=(Exception,),  # This should only retry for exceptions in the sms service
    max_retries=3,
    retry_backoff=4,
    retry_backoff_max=120,
)
def send_user_verification_sms(self, *, user_id):
    user = User.objects.filter(id=user_id).first()
    if user:
        user.send_verification_sms()


@app.task(
    bind=True,
    autoretry_for=(Exception,),  # This should only retry for exceptions in the email service
    max_retries=3,
    retry_backoff=4,
    retry_backoff_max=120,
)
def send_user_verification_email(self, *, user_id):
    user = User.objects.filter(id=user_id).first()
    if user:
        user.send_verification_email()
