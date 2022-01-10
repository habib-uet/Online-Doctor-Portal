from django.db import models

# Create your models here.
class patientlogin(models.Model):
    name=models.CharField(max_length=40)
    Email=models.EmailField(unique=True)
    DOB=models.DateField()
    phone=models.CharField(max_length=13)
    password=models.CharField(max_length=10)
    City=models.CharField(max_length=20)
    cnic=models.CharField(max_length=15)
    lattitude=models.FloatField()
    longitude=models.FloatField()
    image=models.ImageField()
class doctorlogin(models.Model):
    name=models.CharField(max_length=40)
    Email=models.EmailField(unique=True)
    DOB=models.DateField()
    phone=models.CharField(max_length=13)
    password=models.CharField(max_length=10)
    City=models.CharField(max_length=20)
    cnic=models.CharField(max_length=15)
    lattitude=models.FloatField()
    longitude=models.FloatField()
    image=models.ImageField()
    pmdc=models.CharField(max_length=5)
class creditcard(models.Model) :
    name=models.CharField(max_length=40)
    cardbrand=models.CharField(max_length=10)
    cardno=models.CharField(max_length=16)
    expirydate=models.DateField()
    CVV=models.CharField(max_length=3)
    patientid = models.OneToOneField(patientlogin, models.DO_NOTHING)

class easypaisa(models.Model):
    name=models.CharField(max_length=40)
    phone=models.CharField(max_length=13)
    patientid = models.OneToOneField(patientlogin, models.DO_NOTHING)
class jazzcash(models.Model):
    name=models.CharField(max_length=40)
    phone=models.CharField(max_length=13)
    patientid = models.OneToOneField(patientlogin, models.DO_NOTHING)

class doctorcreditcard(models.Model) :
    name=models.CharField(max_length=40)
    cardbrand=models.CharField(max_length=10)
    cardno=models.CharField(max_length=16)
    expirydate=models.DateField()
    CVV=models.CharField(max_length=3)
    doctorid = models.OneToOneField(doctorlogin, models.DO_NOTHING)

class doctoreasypaisa(models.Model):
    name=models.CharField(max_length=40)
    phone=models.CharField(max_length=13)
    doctorid= models.OneToOneField(doctorlogin, models.DO_NOTHING)
class doctorjazzcash(models.Model):
    name=models.CharField(max_length=40)
    phone=models.CharField(max_length=13)
    doctorid = models.OneToOneField(doctorlogin, models.DO_NOTHING)
class makeappointments(models.Model):
    date=models.DateField()
    time=models.TimeField()
    paymentmethod=models.CharField(max_length=30)
    appoointmentstatus=models.CharField(max_length=15)
    patientid=models.ForeignKey(patientlogin,models.DO_NOTHING)
    doctorid=models.ForeignKey(doctorlogin,models.DO_NOTHING)


    
        