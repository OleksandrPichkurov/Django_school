from webbrowser import register

from django.contrib import admin

from .models import (Actor, Category, Genre, Movie, MovieShots, Rating,
                     RatingStar, Reviews)

# Register your models here.

admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(MovieShots)
admin.site.register(Actor)
admin.site.register(Rating)
admin.site.register(RatingStar)
admin.site.register(Reviews)
