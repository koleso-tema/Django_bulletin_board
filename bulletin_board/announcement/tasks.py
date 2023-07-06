import datetime
from celery import shared_task

from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from django.utils import timezone

from announcement.models import Announcement
from bulletin_board.settings import SITE_URL


@shared_task
def mailing_list():
    today = datetime.datetime.now(tz=timezone.utc)
    last_hour = today - datetime.timedelta(hours=1)
    announcement = Announcement.objects.filter(dateCreation__gte=last_hour)
    users = User.objects.all()
    html_content = render_to_string(
        'announcement/mailing_list.html',
        {
            'link': SITE_URL,
            'announcement': announcement,
        }
    )

    msg = EmailMultiAlternatives(
        subject='A new announcements!!!',
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=users,
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()
