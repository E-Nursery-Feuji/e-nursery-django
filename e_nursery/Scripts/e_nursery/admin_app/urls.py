from django.urls import path
from . import views

urlpatterns = [
    path('saveadmin/',views.saveAdmin),
    path('admin/',views.getAdmin)
]