import django_filters
from django.forms import DateTimeInput
from django_filters import FilterSet, DateTimeFilter
from .models import Announcement, Response


# Создаем свой набор фильтров для модели Post.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.
class ResponseFilter(FilterSet):
    title = django_filters.CharFilter(
        field_name="title",
        label='Заголовок',
        lookup_expr='icontains'
    )

    # status = django_filters.ModelChoiceFilter(
    #     field_name='postCategory',
    #     queryset=Response.objects.get('status'),
    #     label='Статус отклика'
    #
    # )
    #
    # author = django_filters.ModelChoiceFilter(
    #     field_name='author',
    #     queryset=Announcement.objects.get('author'),
    #     label='Автор публикации'
    #
    # )


    dateCreate = DateTimeFilter(
        field_name='dateCreation',
        lookup_expr='gte',
        label='Дата создания',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        )
    )
