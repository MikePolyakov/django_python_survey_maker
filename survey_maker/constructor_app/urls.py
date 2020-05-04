from django.urls import path
from constructor_app import views

app_name = 'constructor_app'


urlpatterns = [
    path('', views.main_view),
    path('landing/', views.landing_view),
    path('structure/', views.show_structure),
    path(r'^structure/$', views.show_structure),


]
