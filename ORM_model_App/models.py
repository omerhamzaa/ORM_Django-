from django.db import models
from django.db.models import Model


# Create your models here

class Teacher(models.Model):
    objects = models.Manager()             # class that allows you to perform database query operations on Django models.
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, null=False)
    age = models.IntegerField(null=False)
    subject = models.CharField(max_length=50, null= False)
    email = models.EmailField(unique=True, null=False)
    phone_number = models.CharField(max_length=15, null=False, unique=True)

    def __str__(self):
        return  self.name


class Management(models.Model):
    objects = models.Manager()
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, null=False)
    age = models.IntegerField(null=False)
    designation = models.CharField(max_length=20, null=False)
    phone_number = models.CharField(max_length=11 , null=False)

    def __str__(self):
        return self.designation





class ITDepartment(models.Model):
    object = models.Manager()
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, null=False)
    teacher = models.CharField(max_length=30, null=False)
    session = models.CharField(max_length=10, null=False)
    Email = models.CharField(max_length=50, null=False)
    phone_number = models.CharField(max_length=20, null=False)


    def __str__(self):
        return self.name


class BBIT(models.Model):
    object = models.Manager()
    id = models.AutoField(primary_key=True)
    dep_name = models.CharField(max_length=30, null=False)




    def __str__(self):
        return self.dep_name



class Student(models.Model):
    objects = models.Manager()
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, null=False)
    age = models.IntegerField(null=False, default=0)
    enrolment = models.CharField(max_length=10, null=False)
    subject = models.CharField(max_length=50, null=False)
    email = models.EmailField(unique=True, null=False)
    phone_number = models.CharField(max_length=15, null=False, unique=True)
    Department = models.CharField(max_length=10, null=False)
    # department = models.ManyToManyField(ITDepartment)
    # teachers = models.ManyToManyField(Teacher)
    fk = models.ForeignKey(BBIT, on_delete=models.CASCADE)
    Display_fields = ['id', 'name', 'age', 'enrolment', 'subject', 'email', 'phone_number', 'Department']


    def __str__(self):
        return self.name


