from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import LoginView
from .forms import RegistrationForm
from django.views.generic import CreateView
from .models import User


# Create your views here.
# def get_absolute_url(self):
#     return reverse('user_detail', kwargs={'pk': self.pk})


class UserLoginView(LoginView):
    template_name = 'user_app/login.html'


class UserCreateView(CreateView):
    model = User
    template_name = 'user_app/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('user:login')
