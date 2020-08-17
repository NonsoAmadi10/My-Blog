from . import views
from django.urls import path

urlpatterns = [
    path('register/', views.Register.as_view(), name='register'),
    path('login/', views.login_user, name='login')
]
