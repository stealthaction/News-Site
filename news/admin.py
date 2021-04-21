from django.contrib import admin
from .models import *




class NewsAdmin(admin.ModelAdmin):
    list_display = ['title','content','created_at','updated_at','category', 'is_published']
    list_display_links = ['title','content']
    search_fields = ['title']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']


admin.site.register(Category, CategoryAdmin)
admin.site.register(News, NewsAdmin)

