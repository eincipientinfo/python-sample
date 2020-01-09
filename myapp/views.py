# Create your views here.

from django.shortcuts import render
from django.template import loader
from myapp.form import EmpForm
from django.http import HttpResponse  

def hello(request):  
    return HttpResponse("<h2>Hello, Welcome to Django!</h2>")

def index(request):  
    template = loader.get_template('index.html') # getting our template  
    #       # rendering the template in HttpResponse

    name = {  
            'student':'Test'  
        }  
    return HttpResponse(template.render(name))

#For create Form

def form1(request):
    
    if request.method == "POST":  
        stu = EmpForm(request.POST)  
        if stu.is_valid():  
            try:  
                return redirect('/')  
            except:  
                pass  
    else:  
        stu = EmpForm()  
        
    
    return render(request,"index.html",{'form':stu})

# For set Session
def setsession(request):  
    request.session['sname'] = 'test'  
    request.session['semail'] = 'test.django@gmail.com'  
    return HttpResponse("session is set")  

# For get Session
def getsession(request):  
    studentname = request.session['sname']  
    studentemail = request.session['semail']  
    return HttpResponse(studentname+" "+studentemail); 

# For set Cookie
def setcookie(request):  
    response = HttpResponse("Cookie Set")  
    response.set_cookie('cookie-tutorial', 'New Cookie')  
    return response  

# For get Cookie
def getcookie(request):  
    tutorial  = request.COOKIES['cookie-tutorial']  
    return HttpResponse("New Cookie @: "+  tutorial); 