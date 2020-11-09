import json
import requests
from TracerIND.serializers import (
    PatientInputSerializer,
    PatientOutputSerializer,
    MandalSerializer,
    PHCSerializer,
    VillageSecSerializer,
    VillageSerializer,
)
from doctor.models import Doctor
from hospital.models import Hospital
from mandal.models import Mandal
from patient.models import Patient
from PHC.models import PHC
from village.models import Village
from village_sec.models import Village_sec
from rest_framework.response import Response
from django.shortcuts import render, redirect, HttpResponse
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseServerError
from django.utils.crypto import get_random_string
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError

# LIST APIs
@api_view(["GET"])
def APIView(request):
    APIUrls = [ 
    "GetAllVillage/", 
    "GetAllPatient/",
    "GetAllPHC/",
    "GetAllVillageSec/",
    "GetAllMandal/",
    "AddPatient/",
    "AddPatients/",
    "DeletePatient/",
    "UpdatePatient/",
    "GetPatient/",
    "GetPHCData/",
    "GetVillageSecData/",
    "GetVillageData/",
    "GetPatientData_Village/",
    "login-browse/",
    "token_jwt_get/",
    "token_jwt_refresh/",
    "token_jwt_verify/",
    "GetPVTG/",
    "GetPE/",
    "GetStats/",
    ]
    
    return Response(APIUrls)


# CRUD FOR PATIENT


@api_view(["POST"])
def AddPatient(request):

    try:
        serializer = PatientInputSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400)
    except Exception as e:
        return Response(e)


@csrf_exempt
@api_view(["POST"])
def AddPatients(request):
    try:
        for p in request.data:
            pk = get_random_string(length=16)
            p.update({"pkid": pk})
            p.update({"BasicVitals":{}})
            p.update({"BasicSymptoms":{}})
            p.update({"report":{}})
            try:
                p_village = (Village.objects.get(name__iexact=p["village"])).village_id
            except Exception as e:
                pass
            p.update(village=p_village)
            serializer = PatientInputSerializer(data=p)
            if serializer.is_valid():
                serializer.save()
            else:
                pass
                return Response(serializer.errors, status=400)
        return Response(status=200)
    except Exception as e:
        return Response(e)


@api_view(["POST"])
def DeletePatient(request):
    pk = request.data.get("pkid")
    try:
        patient = Patient.objects.get(pkid=pk)
        patient.delete()
        return Response(status=200)
    except Exception as e:
        return Response(e)


@api_view(["POST"])
def UpdatePatient(request):
    try:
        pk = request.data.get("pkid")
        patient = Patient.objects.get(pkid=pk)
        serializer = PatientInputSerializer(
            instance=patient, data=request.data, partial=True
        )
        if serializers.is_valid():
            serializers.save()
            return HttpResponse(status=200)
        else:
            return Response(serializer.errors, status=400)
    except Exception as e:
        return Response(e)


# PHC for Mandal
@api_view(["POST"])
def GetPHCData(request):
    try:
        phc = PHC.objects.filter(mandal=(request.data.get("mandal_id")))
        serializer = PHCSerializer(phc, many=True)
        return Response(serializer.data, status=200)
    except Exception as e:
        return Response(e)


# VillageSec for PHC
@api_view(["POST"])
def GetVillageSecData(request):
    try:
        villagesec = Village_sec.objects.filter(PHC=(request.data.get("PHC_id")))
        serializer = VillageSecSerializer(villagesec, many=True)
        return Response(serializer.data, status=200)
    except Exception as e:
        return Response(e)


# Village for VillageSec
@api_view(["POST"])
def GetVillageData(request):
    try:
        village = Village.objects.filter(
            village_sec=(request.data.get("villagesec_id"))
        )
        serializer = VillageSerializer(data=village, many=True)
        serializer.is_valid()
        return Response(serializer.data, status=200)
    except Exception as e:
        return Response(e)


# Get All APIs
@api_view(["GET"])
def GetAllVillage(request):
    try:
        villagelist = list(Village.objects.all())
        serializer = VillageSerializer(data=villagelist, many=True)
        serializer.is_valid()
        return Response(serializer.data, status=200)
    except Exception as e:
        return Response(e)

@api_view(["GET"])
def GetAllVillageSec(request):
    try:
        villageseclist = list(Village_sec.objects.all())
        serializer = VillageSecSerializer(data=villageseclist, many=True)
        serializer.is_valid()
        return Response(serializer.data, status=200)
    except Exception as e:
        return Response(e)

@api_view(["GET"])
def GetAllPHC(request):
    try:
        PHClist = list(PHC.objects.all())
        serializer = PHCSerializer(data=PHClist, many=True)
        serializer.is_valid()
        return Response(serializer.data, status=200)
    except Exception as e:
        return Response(e)

@api_view(["GET"])
def GetAllMandal(request):
    try:
        Mandallist = list(Mandal.objects.all())
        serializer = MandalSerializer(data=Mandallist, many=True)
        serializer.is_valid()
        return Response(serializer.data, status=200)
    except Exception as e:
        return Response(e)


@api_view(["GET"])
def GetAllPatient(request):
    try:
        patientlist = Patient.objects.all()
        serializer = PatientOutputSerializer(data=patientlist, many=True)
        serializer.is_valid()
        return Response(serializer.data, status=200)
    except Exception as e:
        return Response(e)


@api_view(["POST"])
def GetPatient(request):
    try:
        pk = request.data.get("pkid")
        patient = Patient.objects.get(pkid=pk)
        serializer = PatientOutputSerializer(patient)
        return Response(serializer.data, status=200)
    except Exception as e:
        return Response(e)


# All Patients in a Village
@api_view(["POST"])
def GetPatientData_Village(request):
    try:
        village = request.data.get("village")
        patientlist = list(
            Patient.objects.filter(
                village=(
                    Village.objects.get(
                        name__iexact=request.data.get("village")
                    ).village_id
                )
            )
        )
        serializer = PatientOutputSerializer(data=patientlist, many=True)
        serializer.is_valid()
        return Response(serializer.data, status=200)
    except Exception as e:
        return Response(e)


# Matrix Analysis
@api_view(["GET"])
def GetPVTG(request):
    try:
        ST_count = Patient.objects.filter(PVTG__iexact="ST").count()
        NST_count = Patient.objects.filter(PVTG__iexact="NST").count()
        total_count = Patient.objects.all().count()
        PVTG_count = total_count - (ST_count+NST_count)
        res = {
            "ST":ST_count,
            "NST":NST_count,
            "PVTG":PVTG_count,
            "Total":total_count
        }
        return Response(res, status=200)
    except Exception as e:
        return Response(e)


@api_view(["GET"])
def GetPE(request):
    try:
        PE = Patient.objects.filter(pedalEdema__iexact="Y")
        PE_count = PE.count()
        bilat = PE.filter(pedal_profile__pedaltype__iexact = "bilateral").count()
        single = PE_count - bilat
        total_count = Patient.objects.all().count()
        res = {
            "total": total_count,
            "PE": PE_count,
            "Bilateral": bilat,
            "Single": single,
        }
        return Response(res, status=200)
    except Exception as e:
        return Response(e)


@api_view(["GET"])
def GetStats(request):
    if request.data.get("params") == "PVTG" :
        Patientlist = Patient.objects.filter(PVTG__iexact = "PVTG")
    else:
        Patientlist = Patient.objects.all()
    try:      
        SC = {
            "Normal": (Patientlist.filter(pedal_profile__serumCreatinine__range=(0,2.0)).count()),
            "MI": Patientlist.filter(pedal_profile__serumCreatinine__range=(2.1, 5.9)).count(),
            "Severe": Patientlist.filter(pedal_profile__serumCreatinine__gt=5.9).count(),
        }

        BU = {
            "Normal": Patientlist.filter(pedal_profile__bloodUrea__range=(15, 40)).count(),
            "Severe": Patientlist.filter(pedal_profile__bloodUrea__gt=40.0).count(),
        }

        ElecSod = {
            "Normal": Patientlist.filter(pedal_profile__electrolytes_sodium__range=(135, 155)).count(),
            "Severe": Patientlist.filter(pedal_profile__electrolytes_sodium__gt=155.0).count(),
        }

        ElecPotas = {
            "Normal": Patientlist.filter(
                pedal_profile__electrolytes_potassium__range=(3.5, 5.5)
            ).count(),
            "Severe": Patientlist.filter(pedal_profile__electrolytes_potassium__gt=5.5).count(),
        }

        BUN = {
            "Normal": Patientlist.filter(pedal_profile__bun__range=(8, 23)).count(),
            "Severe": Patientlist.filter(pedal_profile__bun__gt=23.0).count(),
        }

        UA = {
            "Normal": Patientlist.filter(pedal_profile__uricAcid__range=(2.6, 6.0)).count(),
            "Severe": Patientlist.filter(pedal_profile__uricAcid__gt=6.0).count(),
        }

        res = {
            "SerumCreatinine": SC,
            "BloodUrea": BU,
            "UricAcid": UA,
            "BUN":BUN,
            "Electrolytes_Sodium": ElecSod,
            "Electrolytes_Potassium": ElecPotas,
        }

        return Response(res, status=200)
    except Exception as e:
        return Response(e)


# FOR INIT PURPOSE
# @api_view(["POST"])
# def parseVillage(request):
#     i = 1
#     for item in request.data:
#         vs = {
#             "village_id": i,
#             "name": item.get("Village"),
#             "village_sec": (
#                 Village_sec.objects.get(
#                     name__iexact=(item.get("Village_Sec"))
#                 ).villagesec_id
#             ),
#         }
#         serializer = VillageSerializer(data=vs)
#         if serializer.is_valid():
#             serializer.save()
#             i = i + 1
#         else:
#             print(serializer.errors)
#     return Response("TEST OK")


# @api_view(["POST"])
# def parseVillageSec(request):
#     i = 1
#     for item in request.data:
#         vs = {
#             "villagesec_id": i,
#             "name": item.get("Village_Sec"),
#             "PHC": (PHC.objects.get(name__iexact=(item.get("PHC"))).PHC_id),
#         }
#         serializer = VillageSecSerializer(data=vs)
#         if serializer.is_valid():
#             serializer.save()
#             i = i + 1
#         else:
#             print(serializer.errors)
#     return Response("TEST OK")


# @api_view(["POST"])
# def addmandal(request):
#     serializer = MandalSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(status=200)
#     return Response(serializer.errors)


# @api_view(["POST"])
# def addphc(request):
#     phc = {
#         "PHC_id": request.data.get("PHC_id"),
#         "name": request.data.get("name"),
#         "mandal": (Mandal.objects.get(name=request.data.get("mandal")).mandal_id),
#     }
#     serializer = PHCSerializer(data=phc)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(status=200)
#     return Response(serializer.errors)


# @api_view(["POST"])
# def updatephc(request):
#     phc = PHC.objects.get(PHC_id=request.data.get("PHC_id"))
#     serializer = PHCSerializer(phc, data=request.data, partial=True)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(status=200)
#     return Response(serializer.errors)
