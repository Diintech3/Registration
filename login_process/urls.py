from django.urls import path
from my_app import views

urlpatterns = [
    path('signup/', views.user_signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('users/', views.get_users, name='get_users'),  # ✅ Get all users
]
