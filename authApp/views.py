from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect, render

from authApp.models import User

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def register(request):
    if(request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)

        user = User(username=username, password=password)
        user.save()
        messages.info(request, 'User created successfully')
        return redirect('/')
    
    return render(request, 'register.html')

def login(request):
    if(request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.filter(username=username, password=password)
        if user:
            messages.info(request, 'Login successful')
            request.session['username'] = username
            return redirect('/dashboard')
        else:
            messages.info(request, 'Login failed')
            return redirect('/')
    
    return render(request, 'login.html')

def dashboard(request):
    if 'username' in request.session:
        return render(request, 'dashboard.html', {'username': request.session['username']})
    else:
        return redirect('/')