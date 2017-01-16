from django.contrib import admin
from Movies_REST.models import Person, Role, Movie

# Register your models here.

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):

    list_display = ('first_name', 'last_name', 'birth_date', 'birthplace')

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):

    list_display = ('title', 'director', 'screenplay', 'year', 'genre', 'ranking')


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):

    list_display = ('role', 'actor', 'movie')