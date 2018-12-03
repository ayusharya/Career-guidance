from django.db import models

# Create your models here.
class Table(models.Model):
    no= models.IntegerField(max_length=3,blank=True,null=True)
    School = models.CharField(max_length=500,blank=True,null=True)
    Location = models.TextField(blank=True,null=True)
    SchoolFee = models.IntegerField(blank=True,null=True)
    StartYear = models.DateField(blank=True,null=True)


#python manage.py makemigrations
#python manage.py migrate
    def __str__(self):
        return self.School


class Table2(models.Model):
    no = models.IntegerField(max_length=3,blank=True,null=True)
    School = models.CharField(max_length=500,blank=True,null=True)
    Location = models.TextField(blank=True,null=True)
    SchoolFee = models.IntegerField(blank=True,null=True)
    StartYear = models.DateField(blank=True,null=True)


#python manage.py makemigrations
#python manage.py migrate
    def __str__(self):
        return self.School



class Table3(models.Model):
    no = models.IntegerField(max_length=3,blank=True,null=True)
    School = models.CharField(max_length=500,blank=True,null=True)
    Location = models.TextField(blank=True,null=True)
    SchoolFee = models.IntegerField(blank=True,null=True)
    StartYear = models.DateField(blank=True,null=True)


#python manage.py makemigrations
#python manage.py migrate
    def __str__(self):
        return self.School
