# hospital_management/views.py

from django.shortcuts import render
import requests

def view_patients(request):
    if request.method == 'POST':
        patient_id = request.POST.get("patient_id")
        api_url_patients = 'http://your-api-url-here/patients/{patient_id}'  
        response = requests.get(api_url_patients)
        patients = response.json()
        if response.status_code == 200:
            patients = response.json()
            return render(request, 'view_patients.html', {'patients': patients})

def view_doctors(request):
    if request.method == 'POST':
        doctor_id = request.POST.get("doctor_id")
        api_url_doctors = 'http://your-api-url-here/doctors/{doctor_id}'  
        response = requests.get(api_url_doctors)
        doctors = response.json()
        if response.status_code == 200:
            doctors = response.json()
            return render(request, 'view_doctors.html', {'doctors': doctors})

