"""second_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from second_project.views import index, index2, index3, index4, index5

urlpatterns = [
    path('', index, name='index'),
    path('2/', index2, name='index2'),
    path('3/', index3, name='index3'),
    path('4/', index4, name='index4'),
    path('5/', index5, name='index5'),
    path('admin/', admin.site.urls),
]
