from django import template


from news.models import Category #импортируем модель категория

register = template.Library() #Регистрация библиотек

@register.simple_tag() #декоратор
def get_categories(): #функция будет возвращать получение всех категорий
    return Category.objects.all()


@register.inclusion_tag('news/list_categories.html')
def show_categories(arg1 = 'второй' , arg2 = 'способ'):
    categories = Category.objects.all()
    return {"categories":categories, 'arg1': arg1 , 'arg2': arg2}