import time
from django.db import models
# from django.contrib.postgres.fields import models.JSONField
from django.contrib.auth.models import User
from hospital.models import Hospital
from doctor.models import Doctor

class Patient (models.Model):
    pkid = models.CharField(max_length=32,
                            primary_key=True
                            )
# BASIC DETAILS
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10,blank = True,null = True)
    # adhaar = models.CharField(max_length=256, blank=True)  #hashedData
    relation = models.CharField(max_length=30)  # SonOf/DaughterOf/WifeOf
    gaurdian_name = models.CharField(max_length=50)
    age = models.SmallIntegerField(default=0)
    # M=> Male/F=>Female/NB=>NonBinary
    gender = models.CharField(default='NaN', max_length=3)
    address = models.CharField(max_length=500)
    
    #Bawsic Data
    BasicData = models.JSONField(null = True)
    
    #FORMAT = 
    # {
    # weight = models.DecimalField
    # height = models.DecimalField
    # bloodgroup = models.CharField
    # }

    # Basic Vitals
    BasicVitals = models.JSONField(null=True)

    # FORMAT =
    # {
    # Fever : "xC" for Celcius and "xF",
    # BP : "x",
    # HR : "x",
    # Pulse: "x",
    # RespRate : "x",
    # }

    BasicSymptoms = models.JSONField(null=True)

    # FORMAT =
    # {
    # Temperature : True or False,
    # Aches :  True or False,
    # Fatigue :  True or False,
    # Cold:  True or False,
    # Cough :  True or False,
    # Diarrhoea :  True or False,
    # Bleeding :  True or False,
    # Infection : True or False,
    # others : "Text"
    # }

    report = models.JSONField(null=True)
    # Free For ALL
    habits = models.JSONField(null=True)
    # FORMAT =
    # {
    #    smoking : bool,
    #    drinking : bool
    # }

    doctorreq = models.BooleanField(default=False)
     # if above is yes then ask refer to the following hospital
    PatientStatus = models.JSONField(null = True)
    # hospitalAdmit = models.ForeignKey("app.Model", verbose_name=_(""), on_delete=models.CASCADE)
    # opd = models.BooleanField(default=False)
    # dateOfAdmit = models.CharField(blank=True, max_length=10)  # YYYY-MM-DD
    # refered = models.BooleanField(default=False)
    # # case:yes
    # referredto = models.CharField(max_length=50, blank=True)
    # ref_status = models.TextField(max_length=300, blank=True)
    # treatmentDone = models.TextField(max_length=300, blank=True)
    # DischargeDetails = models.JSONField(null = True)
    #FORMAT = 
    # {
    #     discharged = models.BooleanField()
    # }

    deceased = models.BooleanField(default=False,null = True)
    # if above is answered yes

    DetailsDeath = models.JSONField(null=True)
    # FORMAT =
    {
        # deathDate = models.CharField(blank = True, max_length=10)
        # placeOfDeath = models.CharField(max_length=50,blank=True)
        # causeOfDeath = models.TextField(max_length=300,blank=True)
    }
