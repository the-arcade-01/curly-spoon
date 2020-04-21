from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from accounts import views as accounts_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name = 'home'),
    path('accounts/',include(('accounts.urls','accounts'), namespace = 'accounts')),
    path('host/',include(('AdminApp.urls','AdminApp'), namespace = 'adminapp')),
    path('user/',include(('UserApp.urls','UserApp'), namespace = 'userapp')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
