from django.urls import path
from . import views
urlpatterns = [

    path('saveadmin/',views.registerAdmin),
    path('admin/',views.getAdmin),
    path('updateadmin/<int:id>/',views.update),
    path('updatestatus/<int:id>/',views.status)
]