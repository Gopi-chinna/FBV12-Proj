import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','CRUDFBV12Project.settings')
import django
django.setup()
from MyApps12.models import *
from faker import Faker
from random import *
fakerobj=Faker()

def populate(n):
    for i in range(n):
        feno=randint(1001,9999)
        fename=fakerobj.name()
        fesal=randint(10000,30000)
        feaddr=fakerobj.city()
        emp_record=Employee.objects.get_or_create(eno=feno,ename=fename,esal=fesal,eaddr=feaddr)
        print(emp_record)
populate(10)