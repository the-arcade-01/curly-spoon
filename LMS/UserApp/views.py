from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def profile_views(request):
    return render(request, 'UserApp/profile.html')

def reissue_views(request):
    return render(request, 'UserApp/reissue.html')

def searchbook(request):
    return render(request, 'UserApp/search_book.html')
