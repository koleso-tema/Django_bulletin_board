from django.contrib.auth.models import User, Group
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string

import accounts
from .models import UserCode


@receiver(post_save, sender=User)
def post_save_generate_code(sender, instance, created, *args, **kwargs):
    if created:
        UserCode.objects.create(user=instance)
        instance.is_active = False
        authors_users = Group.objects.get(name="authors")
        instance.groups.add(authors_users)
        instance.save()

        send_mail(
            subject='Welcome to Bulletin Board!',
            message=f'{instance.username}, вы успешно зарегистрировались!'
                    f'Перейдите по ссылке  "http://127.0.0.1:8000/accounts/code" и введите код из '
                    f'сообщения {instance.usercode.code}',
            from_email=None,
            recipient_list=[instance.email],
        )



