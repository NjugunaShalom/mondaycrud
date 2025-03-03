"""
URL configuration for hospital project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from patient import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('diagnosis/', views.diagnosis, name='diagnosis'),
    path('doctor/', views.doctor, name='doctor'),
    path('doctorlist/', views.doctorlist, name='doctorlist'),
    path('diagnosislist/',views.diagnosislist,name='diagnosislist'),
    path('updatedoctor/<int:id>/',views.updatedoctor,name='updatedoctor'),
    path('deletedoctor/<int:id>/',views.deletedoctor,name='deletedoctor'),
    path('updatediagnosis/<int:id>/', views.updatediagnosis, name='updatediagnosis'),
    path('deletediagnosis/<int:id>/', views.deletediagnosis, name='deletediagnosis'),
]
