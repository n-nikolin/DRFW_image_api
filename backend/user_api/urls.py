from django.urls import path, re_path, include
from user_api import views

urlpatterns = [
    path("register", views.UserRegister.as_view(), name="register"),
    path("login", views.UserLogin.as_view(), name="login"),
    path("logout", views.UserLogout.as_view(), name="logout"),
    path("user", views.UserView.as_view(), name="user"),
    # re_path(r"^", include("user_images.urls")),
]
