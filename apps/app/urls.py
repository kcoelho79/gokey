from django.urls import path, re_path
from . import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('CreateResident', views.ResidentCreate, name='CreateResident'),
    # Matches any html file

    re_path(r'^.*\.*', views.pages, name='pages'),

]
