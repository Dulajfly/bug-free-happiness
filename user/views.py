from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy

class Login(LoginView):
    template_name = 'user/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('main')

class MainView(TemplateView):
    template_name = 'main.html'