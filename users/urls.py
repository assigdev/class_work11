from django.urls import path
from .views import UserCreateView, logout_view
from django.contrib.auth.views import LoginView

app_name = 'users'

urlpatterns = [
    path('create_user/', UserCreateView.as_view(), name='create_user'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
]
