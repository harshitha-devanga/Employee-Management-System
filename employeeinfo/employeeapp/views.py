from django.shortcuts import render,redirect,get_object_or_404
from .models import Employee
from .forms import Employeeform
# Create your views here.
def home(request):
    return render(request, 'home.html')
def index(request):
    return render(request, 'index.html')
def viewemployee(request):
    employeelist = Employee.objects.all()
    return render(request, 'viewemployee.html',{'employeelist':employeelist})

def addemployee(request):
    if(request.method == 'POST'):
        form=Employeeform(request.POST,request.FILES)
        if(form.is_valid):
            form.save()
            return redirect(viewemployee)
    else:
        form=Employeeform()
        return render(request,'addemployee.html', {'form':form})

def editemployee(request,pk):
    emp1=get_object_or_404(Employee,pk=pk)
    if(request.method == 'POST'):
        form=Employeeform(request.POST,instance=emp1)
        if(form.is_valid):
            book1=form.save()
            return redirect(viewemployee)
    else:
        form=Employeeform(instance=emp1)
        return render(request,'addemployee.html', {'form':form})

def deleteemployee(request,pk):
    emp1=get_object_or_404(Employee,pk=pk)
    emp1.delete()
    return redirect(viewemployee)