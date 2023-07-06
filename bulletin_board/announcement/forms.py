from django import forms

from announcement.models import Announcement, Response


class AnnouncementCreateForm(forms.ModelForm):
    title = forms.CharField(label='Заголовок')


    class Meta:
        model = Announcement
        fields = [
            'title',
            'category',
            'text',
         ]
        labels = {
            "text": 'Текст объявления',
            'category': 'Выбор категории'
        }


class ResponseCreateForm(forms.ModelForm):
    text = forms.CharField(label='Текст')

    # postCategory = forms.ModelMultipleChoiceField(label='Категория', queryset=Category.objects.all())

    class Meta:
        model = Response
        fields = [
            'text',
        ]
