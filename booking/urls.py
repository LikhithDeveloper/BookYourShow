"""
URL configuration for booking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/',book,name='book'),
    path('time/<id>',time1,name='time1'),
    path('tickets/<id>',tickets,name='tickets'),
    path('movie/',movie,name='movie'),
    path('date/<id>',date,name='date'),
    #path('print/',print,name='print')
    path('login/', login_page, name='login_page'),    # Login page
    path('register/', register_page, name='register'),  # Registration page

] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
