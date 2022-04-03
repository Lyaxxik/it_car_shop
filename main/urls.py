from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('index', views.index, name='index_page'),
    path('login', views.login_view, name='login_page'),
    path('profile', views.profile_page, name='profile_page'),
    path('logout', views.logout_view, name='logout_view'),
    path('register', views.register_view, name='register_page'),
    path('sedan', views.sedan_page, name='sedan_page'),
    path('crossover', views.crossover_page, name='crossover_page')
]
