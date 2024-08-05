from django.urls import path
from rest_framework.routers import SimpleRouter
from . import views

app_name = "accounts"


urlpatterns = [
    path("", views.Login.as_view(), name="login"),
    path("register/", views.Register.as_view(), name="register"),
    path("logout/", views.logout_view, name="logout"),
    path("api/register/", views.RegisterUserAPI.as_view(), name="register_api"),
]
