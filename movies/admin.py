from django.contrib import admin
from .models import MoviesData


# Register your models here.
class MoviesDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'duration', 'rating', 'typ')


admin.site.register(MoviesData, MoviesDataAdmin)
