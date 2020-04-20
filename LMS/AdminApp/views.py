from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def manage_views(request):
    return render(request, 'AdminApp/manage.html')

def issue_views(request):
    return render(request, 'AdminApp/book_issue.html')

def usercreate(request):
    return render(request, 'AdminApp/user_create.html')
