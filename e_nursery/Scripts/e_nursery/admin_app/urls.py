from django.urls import path
from . import views
urlpatterns = [
    path('saveadmin/',views.registerAdmin),
    path('admin/',views.getAdmin)
]