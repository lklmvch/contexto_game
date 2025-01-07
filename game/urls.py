# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('start_game/', views.start_game, name='start_game'),
    path('game/<int:game_id>/', views.play_game, name='play_game'),
    path('game/<int:game_id>/won/', views.won_game, name='won_game'),
]
