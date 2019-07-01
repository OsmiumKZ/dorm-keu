from django.urls import path
from . import views

urlpatterns = [
    path('auth/account/', views.auth_account)
]
