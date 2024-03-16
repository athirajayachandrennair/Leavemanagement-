from email import message
from django.shortcuts import render 
from .models import crud
from .forms import AddForm
from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse

from .forms import regform,AddForm1
from .models import add,users
from django.contrib.auth import authenticate,login as log,logout
from django.contrib.auth.models import User, auth
from django.contrib.auth.models import User, auth





def view(request):
    cr = crud.objects.all()
    return render(request,"view.html",{'cr':cr})

def viewinsert(request):
    cr = add.objects.all()
    return render(request,"viewinsert.html",{'cr':cr})
    
def home(request):
    form = AddForm()
    if request.method =="POST":
        form = AddForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    return render(request,"home.html",{'form':form})


# def homep(request):
#     if request.method=='POST':
#         name = request.POST.get('name')
#         age = request.POST.get('age')
#         email = request.POST.get('email')
#         address = request.POST.get('address')
#         crud(name=name,age=age,email=email,address=address).save()
#     return render(request,'index.html')

def insert(request):
    if request.method=='POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        phonenumber = request.POST.get('phonenumber')
        username = request.POST.get('username')
        password = request.POST.get('password')
        add(firstname=firstname,lastname=lastname,email=email,phonenumber=phonenumber,username=username, password= password).save()
    return render(request,'insert.html')


def hii(request):
    return render(request,'about.html')
    
def index(request):
    return render(request,'index.html')
   
def detailview(request,pk):
    cr = crud.objects.get(id=pk)
    return render(request,"detaileview.html",{'cr':cr})

def login(request):
    return  render(request,'login.html')


def loguser(request):
    if request.method=='POST':

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            log(request,user)
            return  redirect('loggeduser')
        else:
            return render(request,'login.html')
    else:
        return  render(request,'insert.html')

def loggeduser(request):
    return  render(request,'user.html')




def log(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')

        else:
            message.info(request,'invalid credentilas')
            return redirect('log')

    else:
        return render(request,'log.html')

# def signup(request):
#     if request.method=='POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         users(username=username,password=password).save()
#         return  redirect('viewinsert')
#     return render(request, 'userreg.html')

def loguser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        cr = add.objects.filter(username=username, password=password)
        if cr:

           return  redirect('loggeduser')
        else:
            return render(request, 'log.html')

    else:
        return render(request, 'login.html')
