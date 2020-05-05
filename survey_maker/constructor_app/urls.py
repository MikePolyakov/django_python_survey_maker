from django.urls import path
from constructor_app import views

app_name = 'constructor_app'


urlpatterns = [
    path('', views.main_view, name='index'),
    path('companies/', views.CompaniesListView.as_view(), name='companies'),
    # path('company_details/<int:pk>/', views.CompanyDetailView.as_view(), name='company_details'),
    path('company/<int:id>/', views.company, name='company'),
    path('add_company/', views.CompanyCreateView.as_view(), name='add_company'),

    path('landing/', views.landing_view),
    path('structure/', views.show_structure),
    # path(r'^structure/$', views.show_structure)


]
