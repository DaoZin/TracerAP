from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token , refresh_jwt_token , verify_jwt_token
from api import urls as API
from . import views

#CRUD Functionality First, API For ANDROID Next and then API for GettingData and Filtering Data

urlpatterns = [
    path('',views.APIView,name = "APIList"), 
    path('GetAccessLevel/',views.GetAccessLevel,name = "GetAccessLevel"), 
    path('GetAllVillage/',views.GetAllVillage,name = "GetAllVillage"), 
    path('GetAllVillageSec/',views.GetAllVillageSec,name = "GetAllVillageSec"), 
    path('GetAllPHC/',views.GetAllPHC,name = "GetAllPHC"), 
    path('GetAllMandal/',views.GetAllMandal,name = "GetAllMandal"), 
    # path('parseVillage/',views.parseVillage,name = "parseVillage"),
    # path('parseVillageSec/',views.parseVillageSec,name = "parseVillageSec"),
    # path('addmandal/',views.addmandal,name = "addmandal"),
    # path('addphc/',views.addphc,name = "addphc"),
    path('AddPatient/',views.AddPatient,name = "AddPatient"),
    path('AddPatients/',views.AddPatients,name = "AddPatients"),
    path('DeletePatient/',views.DeletePatient,name = "DeletePatient"),
    path('UpdatePatient/',views.UpdatePatient,name = "UpdatePatient"),
    path('GetPatient/',views.GetPatient,name = "GetPatient"),
    path('GetAllPatient/',views.GetAllPatient,name = "GetAllPatient"),
    path('GetPHCData/',views.GetPHCData,name = "GetPHCData"),
    path('GetVillageSecData/',views.GetVillageSecData,name = "GetVillageSecData"),
    path('GetVillageData/',views.GetVillageData,name = "GetVillageData"),
    path('GetPatientData_Village/',views.GetPatientData_Village,name = "GetPatientData_Village"),
    
    #AUTH URLS
    path('login-browse/', include('rest_framework.urls')), #ULTRA EXCLUSIVE DEV API
    path('token_jwt_get/', obtain_jwt_token, name='api_token_jwt'),
    path('token_jwt_refresh/', refresh_jwt_token, name='api_token_jwt'),
    path('token_jwt_verify/', verify_jwt_token, name='api_token_jwt'),
    #ANDROID API
    # path('DroidDump/',views.DroidDump,name = "DroidDump"),

    #Metrics URLS
    path('GetPVTG/', views.GetPVTG, name='GetPVTG'),
    path('GetPE/', views.GetPE, name='GetPE'),
    path('GetStats/', views.GetStats, name='GetStats'),
]