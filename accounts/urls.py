from django.urls import path
from . import views
from .views import csrf


urlpatterns = [
    path('register/', views.UserRegistrationView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('csrf/', csrf, name='csrf'),
    path('current_user/', views.CurrentUserView.as_view(), name='current_user'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    # Add other authentication endpoints as needed
]