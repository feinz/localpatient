from django.shortcuts import render
from django.views import generic

# Create your views here.
from catalog.models import Patient

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    patient_number = Patient.objects.all().count()
    patient_active = Patient.objects.filter(patientstatus__exact='a').count()
    patient_rip = Patient.objects.filter(patientstatus__exact='r').count()   
    patient_mia = Patient.objects.filter(patientstatus__exact='m').count()
    context = {
        'patient_number': patient_number,
        'patient_active': patient_active,
        'patient_rip': patient_rip,
        'patient_mia': patient_mia,
    }
    
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class PatientListView(generic.ListView):
    model = Patient

class PatientDetailView(generic.DetailView):
    model = Patient