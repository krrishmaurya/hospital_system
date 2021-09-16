from django.db import models

class Add_detail(models.Model):

    patient_name=models.CharField(max_length=20)
    contact_no=models.IntegerField()
    addmission_date = models.DateField()
    ward_no = models.IntegerField()
    amount= models.IntegerField()
    disease=models.CharField(max_length=50)
    got_discharge=models.BooleanField(default=False)


class Appointment(models.Model):
    patient_name=models.CharField(max_length=30)
    contact_no=models.IntegerField()
    appointment_date = models.DateField()
    disease=models.CharField(max_length=40)
