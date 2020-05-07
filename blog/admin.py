from django.contrib import admin
from .models import Post, Category, Comment

from django_summernote.admin import SummernoteModelAdmin

class PostAdmin(SummernoteModelAdmin, admin.ModelAdmin):
    summernote_fields = '__all__'
    list_display = ['title', 'category', 'author', 'created']
    search_fields = ['title', 'content']
    list_filter = ('category', 'tags',)

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Comment)
