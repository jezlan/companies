from django.db import models

# Create your models here.
class login(models.Model):
    username= models.CharField(max_length=150)
    password= models.CharField(max_length=150)
    type=models.CharField(max_length=150)
class companydb(models.Model):
    name=models.CharField(max_length=150)
    email=models.CharField(max_length=150)
    description=models.CharField(max_length=150)
    phno=models.BigIntegerField()
    address=models.CharField(max_length=500)
    lid=models.ForeignKey('login',on_delete=models.CASCADE)
class appilcantdb(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    address = models.CharField(max_length=500)
    phno = models.BigIntegerField()
    gender = models.CharField(max_length=150)
    lid = models.ForeignKey('login', on_delete=models.CASCADE)
class qualification(models.Model):
    aid= models.ForeignKey('appilcantdb',on_delete=models.CASCADE)
    clas=models.CharField(max_length=300,default='xx')
    Department = models.CharField(max_length=152)
    yopass = models.CharField(max_length=100)
    institution=models.CharField(max_length=150)
    perofmark=models.IntegerField()
class experience(models.Model):
    aid = models.ForeignKey('appilcantdb', on_delete=models.CASCADE)
    companynme=models.CharField(max_length=150)
    strtdate=models.DateField()
    enddate=models.DateField()
class vaccancy(models.Model):
    cmp_id=models.ForeignKey('companydb',on_delete=models.CASCADE)
    noofvaccany=models.IntegerField()
    jobdetail=models.CharField(max_length=450)
    date=models.DateField(default='2020-01-01')
    qualification=models.CharField(max_length=250)
    salary=models.BigIntegerField()
    Experiance=models.IntegerField()
    status=models.CharField(max_length=250)
class application(models.Model):
    aid = models.ForeignKey('appilcantdb', on_delete=models.CASCADE)
    vid = models.ForeignKey('vaccancy', on_delete=models.CASCADE)
    date =models.DateField()
    status= models.CharField(max_length=250)

class interview(models.Model):
    apid=models.ForeignKey('application',on_delete=models.CASCADE)
    date=models.DateField()
    time=models.CharField(max_length=250)
    place=models.CharField(max_length=250)









