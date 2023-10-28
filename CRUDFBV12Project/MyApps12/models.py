from django.db import models

# Create your models here.
class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=64)
    esal=models.FloatField()
    eaddr=models.CharField(max_length=256)
    def __str__(self):
        return str(self.eno)+"\t"+self.ename+"\t"+str(self.esal)+"\t"+self.eaddr
