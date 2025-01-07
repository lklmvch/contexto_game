from django.contrib import admin

from .models import Game, Guess

# Register your models here.
admin.site.register(Guess)
admin.site.register(Game)
