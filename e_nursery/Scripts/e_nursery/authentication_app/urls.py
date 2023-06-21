from django.urls import path
from . import views
urlpatterns = [
    path('authentication/',views.demo),
]