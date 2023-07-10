from django.urls import path
from . import views
from .views import *

# created by Priya Patel & Samundar Singh Rathore

urlpatterns = [
    # path('',views.demo ),
    path('save/',register_customer,name='register_customer'),
    path('signin/',login_customer,name='login_customer'),
    path('forgotpasswordotp/',forgot_password,name='forgot_password'),
    path('updatepassword/',update_password,name='update_password'),
    path('customerbyemail/<str:email>/', get_customer_by_EMail, name='get_customer_by_EMail')
]