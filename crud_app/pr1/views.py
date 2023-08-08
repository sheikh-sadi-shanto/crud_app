from django.shortcuts import render,redirect
from .form import Form1
from .models import DETAILS,Person,Apk
from django.utils import timezone
# Create your views here.
def home(request):
    all=DETAILS.objects.all()
    if request.method=='POST':
        f=Form1(request.POST,request.FILES)
        today=timezone.now().date()
        if f.is_valid():
            n=f.cleaned_data.get('name')
            im=f.cleaned_data.get('img')

            
            if DETAILS.objects.filter(name=n,created__date=today).exists():
                return redirect('home')
            else:
                obj=DETAILS.objects.create(name=n,pic=im)
                obj.save()
            
    else:
        f=Form1()
    return render(request,'test.html',{'f':f,'all':all})

def index(request):
    return render(request,'index.html')
def modal(request):
    return render(request,'main.html')
def crud(request):
    all=Person.objects.all()
    if request.method=='POST':
        a=request.POST.get('fname')
        b=request.POST.get('lname')
        c=request.POST.get('age')
        d=request.POST.get('gender')
        e=request.POST.get('email')
        f=request.FILES.get('file')
        user=Person(fname=a,lname=b,age=c,gender=d,email=e,pic=f)
        user.save()
    return render(request,'crud.html',{'all':all})
def edit(request,id):
    aa=Person.objects.filter(id=id)
    specific=Person.objects.get(id=id)
    if request.method=='POST':
        a=request.POST.get('fname')
        b=request.POST.get('lname')
        c=request.POST.get('age')
        d=request.POST.get('gender')
        e=request.POST.get('email')
        f=request.FILES.get('file')
        
        specific.fname=a
        specific.lname=b
        specific.age=c
        specific.gender=d
        specific.email=e
        specific.save()
        # user=Person(fname=a,lname=b,age=c,gender=d,email=e)
        # user.save()
    return render(request,'edit.html',{'aa':aa})

def delete(request,id):
    dell=Person.objects.filter(id=id)
    if request.method=='POST':
        dell.delete()
    return redirect('crud')

def apk(request):
    apk_all=Apk.objects.all()
    return render(request,'apk.html',{'app':apk_all})