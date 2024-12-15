"""imc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import re_path as url


from . import views

urlpatterns = [
    
    url(r'^$', views.register , name = ''),
    url(r'^$', views.home , name = 'home'),
    url(r'^toutPerson$', views.toutPerson , name = 'toutPerson'),
    url(r'^showPerson$', views.showPerson , name = 'showPerson'),
    #url(r'^resultat$', views.resultat),
    url('admin/', admin.site.urls),
]