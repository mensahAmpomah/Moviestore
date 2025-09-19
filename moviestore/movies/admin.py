from django.contrib import admin
from .models import Movie
# Register your models here.


class MovieAdmin(admin.ModelAdmin):
    list_display = ['name','price','description']
    ordering = ['name']
    search_fields = ['name']

admin.site.register(Movie, MovieAdmin)