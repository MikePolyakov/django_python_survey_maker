from django.urls import path
from user_app import views
from django.contrib.auth.views import LogoutView


app_name = 'user_app'

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('register/', views.RegisterUserCreateView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('users/', views.UsersListView.as_view(), name='users'),
    path('adduser/', views.UserCreateView.as_view(), name='adduser'),
    path('user/<int:pk>/', views.UserDetailView.as_view(), name='user'),

]
