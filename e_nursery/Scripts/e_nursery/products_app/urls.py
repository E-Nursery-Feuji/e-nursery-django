from django.urls import path
from . import views


urlpatterns = [
    path('image/',views.image),
    path('image/<int:id>/',views.image),
    path('type/',views.type),
    path('type/<int:id>/',views.type),
    path('product/',views.product),
    path('product/<int:id>/',views.product),
    path('blogs/',views.blog),
    path('blogs/<int:id>/',views.blog),
   
]