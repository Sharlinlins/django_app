from django.shortcuts import render, HttpResponse, Http404, redirect, get_object_or_404
from . forms import MNewEmployeeForm
from .models import Employee
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('employee_home', permanent=False)
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:     
        return render(request, 'login.html')
    
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                messages.info(request,'User Created')
                return redirect('login')
        else:
            messages.info(request,'Password Not Matching')
            return redirect('register')
        return redirect('/')

    else:
        return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('index', permanent=False)

def home(request):
    msg = request.session.get("message", None)
    if "message" in request.session:
        del request.session["message"]
        
    emps = Employee.objects.all()[:100]
    return render(request, 'employee_home.html', {"message": msg, 'data': emps})


def new_employee(request):
    if request.method == "GET":
        nef = MNewEmployeeForm()
        return render(request, 'employee_new.html', {'form': nef})
    else:
        nef = MNewEmployeeForm(request.POST)
        if nef.is_valid():
            nef.save()
            request.session["message"] = "New User added"
            return redirect('employee_home', permanent=False)
        else:
            return render(request, 'employee_new.html', {'form': nef})
        
def manage_employee(request, id):
    if request.method == "GET":
    # emp = Employee.objects.filter(id=id)[0]
        emp = Employee.objects.get(pk=id)
        nef = MNewEmployeeForm(instance=emp)
        return render(request, 'employee_manage.html', {'form': nef})
    else:
        
        emp = Employee.objects.get(pk=id)
        nef = MNewEmployeeForm(instance=emp, data=request.POST)
        if nef.is_valid():
            nef.save()
            return redirect('employee_home', permanent=False)
            # return render(request, 'employee_home.html', {'form': nef})
        else:
            return render(request, 'employee_manage.html', {'form': nef})


# def delete_employee(request, id):
#     emp = get_object_or_404(Employee, pk=pk)
#     if request.method =="POST":
#         emp.delete()
#         return redirect('employee_home', permanent=False)
#     else:
#         pass

