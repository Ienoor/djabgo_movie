from django.contrib import admin
from .models import Category, Actor, Gerne, Movie, Rating, RatingStar, Reviews, MovieShorts


admin.site.register(Category)
admin.site.register(Actor)
admin.site.register(Gerne)
admin.site.register(Movie)
admin.site.register(MovieShorts)
admin.site.register(Rating)
admin.site.register(RatingStar)
admin.site.register(Reviews)
