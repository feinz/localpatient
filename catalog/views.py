from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView #easily create,update,view form
from django.urls import reverse_lazy

# Create your views here.
from catalog.models import Patient

@login_required
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    patient_number = Patient.objects.all().count()
    patient_act = Patient.objects.filter(patientstatus__exact='ACT').count()
    patient_rip = Patient.objects.filter(patientstatus__exact='RIP').count()   
    patient_mia = Patient.objects.filter(patientstatus__exact='MIA').count()
    context = {
        'patient_number': patient_number,
        'patient_act': patient_act,
        'patient_rip': patient_rip,
        'patient_mia': patient_mia,
    }
    
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class PatientListView(LoginRequiredMixin, generic.ListView):
    model = Patient
    paginate_by = 20

class PatientDetailView(LoginRequiredMixin, generic.DetailView):
    model = Patient

class PatientCreate(LoginRequiredMixin, CreateView):
    model = Patient
    fields = ['name','ic','address','description','transfer','patientnumber','patientstatus']

class PatientUpdate(LoginRequiredMixin, UpdateView):
    model = Patient
    fields = ['name','ic','address','description','transfer','patientnumber','patientstatus']

class PatientDelete(LoginRequiredMixin, DeleteView):
    model = Patient
    success_url = reverse_lazy('patient_list') #where to redirect after deleted