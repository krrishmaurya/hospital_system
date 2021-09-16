from os import name
from django.urls import path
from . import views
from patient.views import Add_patient, Details,Update_detail,Book_appointment

urlpatterns = [

    path("",views.Home.as_view(),name='home'),
    path("add_patient",Add_patient.as_view(),name='add'),
    path("details/",Details.as_view(),name='detail'),
    path('update_info/',Update_detail.as_view(),name='update'),
    path('login',views.Login.as_view(),name='name'),
    path('logout',views.Logout.as_view(),name='logout'),
    path('appointment',Book_appointment.as_view(),name='appointment'),
    path('view_appointment',views.Display.as_view(),name='display')

]