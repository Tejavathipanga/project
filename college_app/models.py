from django.db import models
from django.core.validators import RegexValidator
class Department(models.Model):
    dep_id=models.IntegerField(unique=True)
    dep=[('ECE','ece'),('CSE','cse'),('CIVIL','civil'),('MECH','mech'),('AI&DS','ai&ds'),('EEE','eee')]
    dep_name=models.CharField(max_length=10,choices=dep)
    def __str__(self):
        return self.dep_name
class Teachers(models.Model):
    teacher_id=models.IntegerField(unique=True)
    teacher_name=models.CharField(max_length=20)
    mobile=RegexValidator(r'^[6-9]{1}[0-9]{9}',
        message="Enter a valid 10-digit mobile number starting with 6-9")
    teacher_mobile=models.CharField(max_length=10,validators=[mobile])
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    def __str__(self):
        return self.teacher_name
class Students(models.Model):
    std_id=models.IntegerField(unique=True)
    std_name=models.CharField(max_length=30)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.std_name

# Create your models here.
