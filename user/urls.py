from django.urls import path, include
from .views import Login as Login

urlpatterns = [
    path('login/', Login.as_view(), name='login')
]
