"""dpa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import include
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from pizza import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pizza.urls')),
    url(r'^api/pizzalist/', views.pizzaList.as_view(), name = 'pizzalist'),
    url(r'^api/pizalter/(?P<pid>\d+)/', views.pizzaAlter.as_view(), name = 'pizalter'),
    url(r'^api/pizadd/', views.pizzaCreate.as_view(), name = 'pizadd'),


    
]