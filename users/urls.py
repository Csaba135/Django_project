from django.urls import path
from users.views import login_view, register_view, logout_view, customer_view
app_name = 'users'

urlpatterns = [
     path('login/', login_view, name='login'),
     path('register/', register_view, name='register'),
     path('logout/', logout_view, name='logout'),
     path('customer/', customer_view, name='customer'),
]