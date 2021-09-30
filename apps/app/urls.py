from django.urls import path, re_path
from . import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('CreateResident', views.ResidentCreate.as_view(), name='CreateResident'),
    path('ResidentImport', views.ResidentImport, name='ResidentImport'),
    path('ListResident', views.ResidentList.as_view(), name='ListResident'),
    path('ResidentDelete/<int:id>', views.ResidentDelete, name='ResidentDelete'),
    path('EventList', views.EventList, name='EventList'),
    path('EventDelete/<int:id>', views.EventDelete, name='EventDelete'),
    path('EventDeleteAll', views.EventDeleteAll, name='EventDeleteAll'),

    # Matches any html file

    re_path(r'^.*\.*', views.pages, name='pages'),

]
