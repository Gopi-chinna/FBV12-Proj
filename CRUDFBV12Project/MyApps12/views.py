from django.shortcuts import render,redirect
from MyApps12.forms import EmployeeForm
from MyApps12.models import Employee
# Create your views here.
def show_view(request):
    employees=Employee.objects.all()
    return render(request,'MyApps12/index.html',{'employees':employees})

def insert_view(request):
    form=EmployeeForm()
    if request.method=="POST":
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/index')
    return render(request,'MyApps12/insert.html',{'form':form})

def delete_view(request,pk):
    employee=Employee.objects.get(id=pk)
    employee.delete()
    return redirect('/index')
def update_view(request,pk):
    employee=Employee.objects.get(id=pk)
    if request.method=='POST':
        form=EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
            return redirect('/index')
    return render(request,'MyApps12/update.html',{'employee':employee})