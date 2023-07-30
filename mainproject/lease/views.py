from django.shortcuts import render, HttpResponse, redirect
from.models import register, uploaddata
# Create your views here.
def registerpageuser(request):
    if request.method == 'POST':
        getname=request.POST.get('name')
        getaddress = request.POST.get('address')
        getusername = request.POST.get('username')
        getpassword = request.POST.get('password')
        users=register()
        users.Name=getname
        users.Address=getaddress
        users.Username=getusername
        users.Password=getpassword
        users.save()
    return render(request,'registerpagesuser.html')

def userlogin(request):
    if request.method == 'POST':
        getusername=request.POST.get('username')
        getpassword=request.POST.get('password')
        try:
            register.objects.get(Username=getusername,Password=getpassword)
            return HttpResponse('Welcome User')
        except:
            return HttpResponse('Invalid User')
    return render(request,'userlogin.html')

def adminlog(request):
    if request.method == 'POST':
        getusername = request.POST.get('username')
        getpassword = request.POST.get('password')
        if getusername == 'admin' and getpassword == 'admin':
            return HttpResponse('Welcome Admin')
        else:
            return HttpResponse('Invalild')
    return render(request, 'adminlogin.html')

def operationuser(request):
    details=register.objects.all()
    return render(request,'operationuser.html',{'value':details})

def edituser(request,id):
    details=register.objects.all()
    users=register.objects.get(id=id)
    if request.method == 'POST':
        getaddress = request.POST.get('address')
        getpassword = request.POST.get('password')
        users.Address = getaddress
        users.Password = getpassword
        users.save()
        return redirect('/operationuser')
    return render(request,'operationuser.html',{'value':details,'data':users})

def deleteuser(request,id):
    data=register.objects.filter(id=id).delete()
    return redirect('/operationuser')

def pendinguser(request):
    details = register.objects.filter(Status=False)
    return render(request,'pendinguser.html',{'value':details})

def approveuser(request,id):
    getdata = register.objects.get(id = id)
    getdata.Status=True
    getdata.save()
    return redirect('/pendinguser')

def approveduser(request):
    details = register. objects.filter(Status=True)
    return render(request, 'approveduser.html', {'value': details})

def registerpagecontainer(request):
    if request.method=='POST':
        getname=request.POST.get('name')
        getidno=request.POST.get('idno')
        getprice=request.POST.get('price')
        getpicture=request.FILES['picture']
        file=uploaddata()
        file.Name=getname
        file.Idno=getidno
        file.Price=getprice
        file.Picture=getpicture
        file.save()
    return render(request, 'registerpagecontainer.html')

def pending(request):
    details=uploaddata.objects.filter(Status=False)
    return render(request,'pendinglist.html',{'value':details})

def approve(request,id):
    getdata = uploaddata.objects.get(id = id)
    getdata.Status=True
    getdata.save()
    return redirect('/pending')

def approved(request):
    details = uploaddata.objects.filter(Status=True)
    return render(request, 'approvedlist.html', {'value': details})

def operationcontainer(request):
    details=uploaddata.objects.all()
    return render(request,'operationcontainer.html',{'value':details})

def editcontainer(request,id):
    details=uploaddata.objects.all()
    users=uploaddata.objects.get(id=id)
    if request.method == 'POST':
        getname = request.POST.get('name')
        getprice = request.POST.get('price')
        getpicture = request.FILES.get('picture')
        users.Name = getname
        users.Price = getprice
        if getpicture:
            users.Picture = getpicture

        users.save()
        return redirect('/operationcontainer')

        users.save()
        return redirect('/operationcontainer')
    return render(request,'operationcontainer.html',{'value':details,'data':users})

def deletecontainer(request,id):
    data=uploaddata.objects.filter(id=id).delete()
    return redirect('/operationcontainer')
