from django.urls import path
from .views import home, register, user_login, user_logout, profile, profile_view

app_name = "main_app"

urlpatterns = [
    path("", home, name="home"),
    path("auth/register/", register, name="register"),
    path("auth/login/", user_login, name="login"),
    path("auth/logout/", user_logout, name="logout"),
    path("profile/", profile, name="profile"),
    path("profile/view/", profile_view, name="profile_view"),
]