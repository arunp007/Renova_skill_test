from django.shortcuts import render, redirect
from django.http import HttpResponse
from.models import *

def login(request):
    email = None
    password = None
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
    try: 
        current_user = Registration.objects.get(email = email, password = password)
        request.session['xyz'] = current_user.id
        return redirect('home')
    except Registration.DoesNotExist:
        return render(request, 'login.html', {'message': "Email Id And Password Is Wrong"})

def signup(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        auth = request.POST['auth']
        user_data = Registration(fullname = fullname, phone = phone, email = email, password = password, cpassword = cpassword, auth = auth)
        user_data.save()
    return render(request,'signup.html')

def home(request):
    return render(request, 'home.html')

def logout(request):
    request.session.flush()
    return redirect('login')

def user_table(request):
    user_data = Registration.objects.all()
    return render(request, 'user.html', {'user': user_data})

def delete(request,id):
    Registration.objects.get(id = id).delete()
    return redirect('user_table')

def update(request, id):
    update_data = ""
    if request.method == 'POST':
        fullname = request.POST['fullname']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        auth = request.POST['auth']
        Registration.objects.filter(id=id).update(fullname = fullname, phone = phone, email = email, password = password, cpassword = cpassword, auth = auth)
        return redirect('user_table')
    
    else:
        update_data = Registration.objects.get(id = id)
        return render(request, 'signup.html', {'update': update_data})
