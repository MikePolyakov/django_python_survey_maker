from django.urls import path
from constructor_app import views

app_name = 'constructor_app'


urlpatterns = [

    path('companies/', views.CompaniesListView.as_view(), name='companies'),
    path('company/<int:pk>/', views.CompanyDetailView.as_view(), name='company'),
    path('create/', views.CompanyCreateView.as_view(), name='create'),
    path('landing/', views.landing_view),

]
