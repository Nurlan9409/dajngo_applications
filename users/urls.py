from django.urls import path
from .views import users_page,about_page
urlpatterns = [
    path('users/', users_page),
    path('about/', about_page),
]