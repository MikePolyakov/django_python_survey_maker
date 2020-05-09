from django.urls import path
from maker_app import views

app_name = 'maker_app'


urlpatterns = [
    path('', views.main_view, name='index'),
    path('companies/', views.CompaniesListView.as_view(), name='companies'),
    path('company/<int:pk>/', views.CompanyDetailView.as_view(), name='company'),
    path('create/', views.CompanyCreateView.as_view(), name='create'),
    path('landing/', views.landing_view),

]
