from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from patient.forms import PatientForm, DiagnosisForm,DoctorForm
from patient.models import Doctor, Diagnosis


# Create your views here.
def index(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PatientForm()
    return render(request, 'index.html',{'form': form})

def diagnosis(request):
    if request.method == "POST":
        form = DiagnosisForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('diagnosis')
    else:
        form = DiagnosisForm()
    return render(request, 'diagnosis.html',{'form': form})

def doctor(request):
    if request.method == "POST":
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctor')
    else:
        form = DoctorForm()
    return render(request, 'doctor.html',{'form': form})

def doctorlist(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctorlist.html',{'doctors': doctors})

def diagnosislist(request):
    diagnosiss = Diagnosis.objects.all()
    return render(request, 'diagnosislist.html',{'diagnosiss': diagnosiss})

def updatedoctor(request,id):
    doctor = get_object_or_404(Doctor, id=id)
    if request.method == "POST":
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('doctorlist')
    else:
        form = DoctorForm(instance=doctor)
    return render(request, 'updatedoctor.html', {'form': form,'doctor': doctor})

def deletedoctor(request,id):
    doctor = get_object_or_404(Doctor, id=id)
    try:
        doctor.delete()
    except Exception as e:
        messages.error(request, 'Doctor not deleted')
    return redirect('doctorlist')

def updatediagnosis(request,id):
    diagnosis = get_object_or_404(Diagnosis, id=id)
    if request.method == "POST":
        form = DiagnosisForm(request.POST, instance=diagnosis)
        if form.is_valid():
            form.save()
            return redirect('diagnosislist')
    else:
        form = DiagnosisForm(instance=diagnosis)
    return render(request, 'updatediagnosis.html', {'form': form,'diagnosis': diagnosis})

def deletediagnosis(request,id):
    diagnosis = get_object_or_404(Diagnosis, id=id)
    try:
        diagnosis.delete()
    except Exception as e:
        messages.error(request, 'Diagnosis not deleted')
    return redirect('diagnosislist')