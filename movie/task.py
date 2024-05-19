from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_email(to_emails):
    send_mail(
        "Thanks",
        "Thanks for rating this movie",
        from_email=None,
        recipient_list=[to_emails],
        fail_silently=False,
    )
