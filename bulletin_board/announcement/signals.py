from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from announcement.models import Response


@receiver(post_save, sender=Response)
def post_save_response_accept(sender, instance, created, **kwargs):
    response_author = instance.author.username
    announcement_author = instance.announcement.author.username
    text = instance.text
    if instance.status == 1:
        subject = f' Your response accepted by author {announcement_author}'

        send_mail(
            subject=subject,
            message=text,
            from_email=None,
            recipient_list=[instance.author.email],
        )
    if created:
        subject = f' The new response from user {response_author}'

        send_mail(
            subject=subject,
            message=text,
            from_email=None,
            recipient_list=[instance.announcement.author.email],
        )
