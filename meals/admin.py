from django.contrib import admin
from .models import Meals, Category

from django_summernote.admin import SummernoteModelAdmin

class MealsAdmin(SummernoteModelAdmin, admin.ModelAdmin):
    summernote_fields = '__all__'
    list_display = ['name', 'price', 'preparation_time', 'people']
    search_fields = ['category', 'people', 'slug']
    list_filter = ('people', 'price', 'slug', 'category')

admin.site.register(Meals, MealsAdmin)
admin.site.register(Category)
