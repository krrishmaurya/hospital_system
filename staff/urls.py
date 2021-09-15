from os import name
from django.urls import path
from . import views
from patient.views import Add_patient, Details,Update_detail

urlpatterns = [

    path("",views.Home.as_view(),name='home'),
    path("add_patient",Add_patient.as_view(),name='add'),
    path("details/",Details.as_view(),name='detail'),
    path('update_info/',Update_detail.as_view(),name='update')

]