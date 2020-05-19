from django.contrib import admin
from .models import Meals, Category



class MealsAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'preparation_time', 'people']
    search_fields = ['category', 'people', 'slug']
    list_filter = ('people', 'price', 'slug', 'category')

admin.site.register(Meals, MealsAdmin)
admin.site.register(Category)
