from django.urls import path, re_path
from . import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('CreateResident', views.ResidentCreate.as_view(), name='CreateResident'),
    path('ListResident', views.ResidentList.as_view(), name='ListResident'),

    # Matches any html file

    re_path(r'^.*\.*', views.pages, name='pages'),

]
