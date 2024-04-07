from django.urls import path
from .views import StudentLisView,MainView
urlpatterns = [
    path('users/', StudentLisView.as_view(),name="users_page"),
    path('', MainView.as_view(),name="main"),
]