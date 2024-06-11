from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("signIn/", views.sign_up, name="sign_Up"),
    path("logout/", views.logout_view, name="logout"),
]
