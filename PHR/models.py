from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class DocumentCategoryMaster(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=50,null=True,blank=True)
    short_description=models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.name

class PurposeMaster(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=50,null=True,blank=True)
    short_description=models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.name

class HospitalMaster(models.Model):
    hospital_name=models.CharField(max_length=50)
    email=models.CharField(max_length=50,null=True,blank=True)
    phone=models.CharField(max_length=200,null=True,blank=True)
    address=models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.hospital_name

class Patient_Profile(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    first_name=models.CharField(max_length=50)
    middle_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    age=models.CharField(max_length=50)
    dob=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    blood_group=models.CharField(max_length=50)
    marital_status=models.CharField(max_length=50)
    father_name=models.CharField(max_length=50)
    mobile_number=models.CharField(max_length=50)
    email_id=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    country=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    pin_code=models.CharField(max_length=50)
    profile_photo=models.CharField(max_length=50)

class Prescription_Detail(models.Model):
    prescrip_no=models.CharField(max_length=50)
    date=models.DateField()
    doc_type=models.ForeignKey(DocumentCategoryMaster,on_delete=models.CASCADE)
    purpose=models.ForeignKey(PurposeMaster,on_delete=models.CASCADE)
    document=models.FileField(upload_to='prescription/',blank=True)
    hospital=models.ForeignKey(HospitalMaster,on_delete=models.CASCADE)
    doctor=models.CharField(max_length=50)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)

