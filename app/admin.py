from django.contrib import admin
from .models import Library,Books

# Register your models here.

class LibraryAdmin(admin.ModelAdmin):
    list_display = ('name','id','location')
    search_fields = ('name','id')
    list_filter = ('location',)

admin.site.register(Library,LibraryAdmin)
admin.site.register(Books)