from django.db import models

class Myuser(models.Model):
    username= models.CharField(max_length=20)
    password=models.CharField(max_length=10)
class Intake(models.Model):#ORM
    id=models.AutoField(primary_key=True)
    intakename=models.CharField(max_length=30)
    startdate=models.DateField()
    enddate=models.DateField()