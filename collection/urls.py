from django.urls import path
from . import views
from .views import buscar_elementos

urlpatterns = [
    path("", views.index, name="index"),
    path("accounts/profile/", views.index, name="index"),
    path("accounts/register/", views.register, name="register"),
    path('buscar/', buscar_elementos, name='buscar_elementos')
]
