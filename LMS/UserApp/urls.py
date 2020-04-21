from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('profile/',views.profile_views, name = 'profile'),
    path('reissue/',views.reissue_views, name = 'reissue'),
    path('searchbook/',views.searchbook, name = 'searchbook'),
]
