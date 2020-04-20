from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('manage/',views.manage_views, name = 'manage'),
    path('issue/',views.issue_views, name = 'issue'),
    path('usercreate/',views.usercreate, name = 'usercreate'),
]
