from django.db import models

# Create your models here.
class employee(models.Model):
    emp_num = models.IntegerField()
    emp_name = models.CharField(max_length=64)
    emp_sal = models.FloatField()
    emp_dept = models.CharField(max_length = 64)
    emp_add = models.CharField(max_length = 128)
