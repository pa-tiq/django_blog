from django.urls import path
from auth_app import views

# app_name is a keyword. With it, I register the namespace of the app.
app_name = 'auth_app'

urlpatterns = [
    path("", views.register, name="register"),
    path("register/", views.register, name="register"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout")
]
