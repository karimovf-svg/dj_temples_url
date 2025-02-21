from django.contrib import admin
from .models import Cars, Carmodel

class CarsAdmin(admin.ModelAdmin):
    list_display = ('title', 'photo', 'color', 'ot_kuchi', 'year', 'price')
    list_display_links = ['title']
    search_fields = ['title']
    list_editable = ['title']

class CarmodelAdmin(admin.ModelAdmin):
    list_display = ('title', 'context')
    list_display_links = ['title']
    search_fields = ['title']
    list_editable = ['title']

admin.site.register(Carmodel)
admin.site.register(Cars)