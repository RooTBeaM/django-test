from turtle import title
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Blog,Author, Contact


# Register your models here.
# admin.site.register(Blog)

class BlogAdmin(SummernoteModelAdmin):
    """"Register model by ModelAdmin"""
    list_display = ('title','author','date_created','date_updated')
    summernote_fields = '__all__'
    # summernote_fields = ('content',)

admin.site.register(Blog, BlogAdmin)
admin.site.register(Author)
admin.site.register(Contact)
