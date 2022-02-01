from cgitb import html
from multiprocessing import context
from re import M
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Myuser
from datetime import date
from .models import Intake
# Create your views here.

def home(request):
    html = """
    
   <!DOCTYPE html>
    <html lang="en">
     <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
     </head>
    <link
    rel="stylesheet"
    href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
    integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm"
    crossorigin="anonymous"
     />
    <body>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <a class="navbar-brand" href="#">Navbar</a>
      <button
        class="navbar-toggler"
        type="button"
        data-toggle="collapse"
        data-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item active">
            <a class="nav-link" href="#">Home <span class="sr-only"></span></a>
            <a class="nav-link" href="about"
              >About <span class="sr-only"></span
            ></a>
            <a class="nav-link" href="contact"
              >Contact Us <span class="sr-only"></span
            ></a>
          </li>
                        </ul>
             </div>
            </nav>
            <h1>WELCOME</h1>
        </body>
        </html>
            """
    return HttpResponse(html)
def about(request):
    return render(request,'pages/about.html')
def landing (request):
  return render(request,'pages/landing.html')

def contact (request):
    return render(request,'pages/contact.html')
def login(request):
  if (request.method=="GET"):
    return render(request,'pages/login.html')
    print("if cond")
  else:
     user= Myuser.objects.filter(username=request.POST['username'],password=request.POST['password'])
     print("else cond",request)
     if(len(user)>0):
       return redirect(landing)
     else:
       context={}
       context['warning']='Invalid username or password'
       return render(request,'pages/login.html',context)
       
def register(request):
  if (request.method=='GET'):
    return render(request,'pages/register.html' )
  else:
   
      Myuser.objects.create(username=request.POST['username'],password=request.POST['password'])
      return render (request, 'pages/login.html')
def insert(request):
  context={}
  if(request.method=='GET'):
    return render(request,'pages/insert.html',context)
  else:
    print(request.POST)
    name=request.POST['name']
    sdate=date.today()
    endate=date.today()
    Intake.objects.create(intakename=name,startdate=sdate,enddate=endate)
    intakes=Intake.objects.all()
    context['intakes']=intakes

    
   
    return render(request,'pages/list.html',context)
def updateintake(request,id):
    context={}
    Intake.objects.filter(id=id).update()
    intakes = Intake.objects.all()
    context['intakes'] = intakes
    return render(request, 'pages/list.html', context)
def deleteintake(request,id):
    context={}
    Intake.objects.filter(id=id).delete()
    intakes = Intake.objects.all()
    context['intakes'] = intakes
    return render(request, 'pages/list.html', context)