from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponse
# Create your views here.

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            # for testing purpose giving an http response
            return HttpResponse('<h1>signup</h1>')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html',{'form':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
            # for testing purpose giving an http response
                return HttpResponse('<h1>login</h1>')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html',{'form':form})

# logout func to be added
