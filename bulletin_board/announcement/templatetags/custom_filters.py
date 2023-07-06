from django import template

register = template.Library()


# Регистрируем наш фильтр под именем currency, чтоб Django понимал,
# что это именно фильтр для шаблонов, а не простая функция.
@register.filter()
def censor(text):
    censor_words = [
        'редиска', 'Убийство', 'Война', 'ИГИЛ'
    ]
    if type(text) != str:
        raise TypeError('Данные не являются строкой')

    for word in text.split():
        if word in censor_words:
            text = text.replace(word, f"{word[0]}{'*' * (len(word) - 1)}")


    return f'{text}'

