from django.urls import path

from . import views


app_name = "users"

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name="login"),
    path('register/', views.RegisterView.as_view(), name="register"),
    path('logout/', views.logout, name='logout'),
]
