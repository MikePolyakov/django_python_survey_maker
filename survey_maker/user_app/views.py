from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import LoginView
from .forms import RegistrationForm
from django.views.generic import ListView, DetailView, CreateView
from .models import User


# Create your views here.
# def get_absolute_url(self):
#     return reverse('user_detail', kwargs={'pk': self.pk})


class UserLoginView(LoginView):
    template_name = 'user_app/login.html'


class RegisterUserCreateView(CreateView):
    model = User
    template_name = 'user_app/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('user:login')


# ListView
class UsersListView(ListView):
    model = User
    template_name = 'user_app/users.html'


# CreateView
class UserCreateView(LoginRequiredMixin, CreateView):
    fields = ('email', 'first_name', 'last_name', 'avatar')

    model = User
    success_url = reverse_lazy('user:users')
    template_name = 'user_app/adduser.html'

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        return super().form_valid(form)


# DetailView
class UserDetailView(UserPassesTestMixin, DetailView):
    model = User
    template_name = 'user_app/user.html'

    def test_func(self):
        return self.request.user.is_superuser
