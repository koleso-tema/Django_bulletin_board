from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Announcement(models.Model):
    TYPE = (
        ('tank', 'Танки'),
        ('heal', "Хилы"),
        ('dd', "ДД"),
        ('buyers', 'Торговцы'),
        ('gildmaster', 'Гилдмастеры'),
        ('quest', 'Квестгиверы'),
        ('smith', 'Кузнецы'),
        ('tanner', 'Кожевники'),
        ('potion', 'Зельевары'),
        ('spellmaster', 'Мастера заклинаний'),
    )
    dateCreation = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, unique=False, on_delete=models.CASCADE, null=False, blank=True)
    category = models.CharField(max_length=11, choices=TYPE, default='tank')
    title = models.CharField(max_length=64)
    text = RichTextUploadingField()

    def __str__(self):
        return f'{self.title}:{self.author}:{self.category}:{self.text}'

    def get_absolute_url(self):
        return reverse('anno_detail', args=[str(self.id)])


class Response(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE, related_name='anno_to_ammo',)
    status = models.BooleanField(default=False)
    dateCreation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.text}:{self.author}:{self.status}'

    def get_absolute_url(self):
        return reverse('personal_area', args=[str(self.id)])