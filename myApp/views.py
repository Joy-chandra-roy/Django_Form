from django.shortcuts import render,redirect
from myApp.forms import studentForm
from myApp.models import student

# Create your views here.
def home(request):
    form=studentForm()
    if request.method=="POST":
        n=request.POST.get('name')
        e=request.POST.get('email')
        a=request.POST.get('address')
        print(n,e,a)  
        student.objects.create(name=n, email=e, address=a)
        return redirect('table')
    return render(request, "index.html",{"f":form})

def read(request):
    data=student.objects.all()
    return render (request, "read.html",{"d":data})

def delItem(request, pk):
    data=student.objects.get(id=pk)
    data.delete()
    
    return redirect('table')

def upItem(request,pk):
    data=student.objects.get(id=pk)
    form=studentForm(initial={'name':data.name, 'email':data.email, 'address':data.address})
    if request.method=="POST":
        n=request.POST.get('name')
        e=request.POST.get('email')
        a=request.POST.get('address')
        
        obj=student(name=n, email=e, address=a)
        obj.id=pk
        obj.save()
        return redirect('table')
    return render(request, "update.html",{"f":form})