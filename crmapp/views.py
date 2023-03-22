from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from crmapp.models import Register_Table
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request):
    # if request.method == 'POST':
    #     form = UserCreationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('home')
    # else:
    #     form = UserCreationForm()
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        uname = request.POST['username']
        email = request.POST['email']
        pwd = request.POST['password']
        cont = request.POST['contact']
        dept = request.POST['dept']
        
        usr = User.objects.create_user(uname,email,pwd)
        usr.first_name = fname
        usr.last_name = lname
        
        if dept == "manager":
            usr.is_staff = True
        usr.save()

        reg = Register_Table(user=usr, contact=cont)
        reg.save()
        return render(request, 'crmapp/signup.html', {"status":" Mr/Miss. {} You Have Registerd Successfully".format(fname)})

    return render(request, 'crmapp/signup.html')

def check_user(request):
    if request.method == 'GET':
        uname = request.GET["user_name"]
        check = User.objects.filter(username=uname)
        if len(check) == 1:
            return HttpResponse("Exist")
        else:
            return HttpResponse("User Not Exist")

def user_login(request):
    if request.method == 'POST':
        uname = request.POST['username']
        pwd = request.POST['password']
        user = authenticate(username=uname,password=pwd)
        if user:
            login(request,user)
            if user.is_superuser:
                return HttpResponseRedirect('admin')
            if user.is_staff:
                return HttpResponseRedirect('manager_dashboard')
            if user.is_active:
                return HttpResponseRedirect('emp_dashboard')
        else:
            return render(request, 'home.html', {"status":"Invalid User"})
    return HttpResponse("Login")
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required
def manager_dashboard(request):
    data = Register_Table.objects.get(user__id=request.user.id)
    return render(request,'crmapp/manager_dashboard.html', {'data':data})

@login_required
def emp_dashboard(request):
    data = Register_Table.objects.get(user__id=request.user.id)
    return render(request,'crmapp/emp_dashboard.html', {'data':data})

def view_profile(request):
    data = Register_Table.objects.get(user__id=request.user.id)
    return render(request,'crmapp/view_profile.html', {'data':data})

def edit_profile(request):
    context = {}
    data = Register_Table.objects.get(user__id=request.user.id)
    context["data"]=data
    if request.method == 'POST':
        fn = request.POST['fname']
        ln = request.POST['lname']
        em = request.POST['email']
        cont = request.POST['contact']
        age = request.POST['age']
        city = request.POST['city']
        gen = request.POST['gender']
        occ = request.POST['occupation']
        about = request.POST['about']
        
        usr = User.objects.get(id=request.user.id)
        usr.first_name = fn
        usr.last_name = ln
        usr.email = em
        usr.save()
        
        data.contact = cont
        data.age = age
        data.city = city
        data.gender = gen
        data.occupation = occ
        data.about = about
        data.save()
        
        if 'image' in request.FILES:
            img = request.FILES['image']
            data.profile_pic = img
            data.save()
             
        context['status'] = "Changes saved successfully"
    return render(request, 'crmapp/edit_profile.html', context)