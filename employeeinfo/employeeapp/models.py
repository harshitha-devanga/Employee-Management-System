from django.db import models

# Create your models here.
class Employee(models.Model):
    g=[
        ('FEMALE','FEMALE'),
        ('MALE','MALE'),
    ]


    profile=models.ImageField(upload_to='profile_images/',null=True)
    eid=models.AutoField(primary_key=True)
    ename=models.CharField(max_length=50)
    egender=models.CharField(choices=g,max_length=50)
    eage=models.IntegerField()
    email=models.EmailField(null=True,unique=True)
    esalary=models.IntegerField()
    doj=models.DateField(null=True)
    eyoe=models.CharField(max_length=200)
    edep=models.CharField(max_length=200)
    company=models.CharField(max_length=200)
    def  __str__(self):
        return self.ename