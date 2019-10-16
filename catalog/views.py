from django.shortcuts import render
from django.views import generic
from django.db.models import Q #to query multiple filter
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView #easily create,update,view form
from django.urls import reverse_lazy

# importing Patient models
from catalog.models import Patient

@login_required
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    patient_number = Patient.objects.all().count()
    patient_act = Patient.objects.filter(patient_status__exact='ACT').count()
    patient_rip = Patient.objects.filter(patient_status__exact='RIP').count()   
    patient_mia = Patient.objects.filter(patient_status__exact='MIA').count()
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
        paginate_by = 10
        # search function
        def get_queryset(self):
            query = self.request.GET.get('q')
            if query:
                object_list = self.model.objects.filter(Q(name__contains=query) | Q(identity_card_number__contains=query) | Q(address__contains=query) | Q(description__contains=query) | Q(transfer__contains=query) | Q(patient_number__contains=query) | Q(patient_status__contains=query))
            else:
                object_list = self.model.objects.all()
            return object_list

class PatientDetailView(LoginRequiredMixin, generic.DetailView):
    model = Patient

class PatientCreate(LoginRequiredMixin, CreateView):
    model = Patient
    fields = ['name','identity_card_number','address','description','transfer','patient_number','patient_status','time_registered']
    success_url = reverse_lazy('patient_create') #where to redirect after create

class PatientUpdate(LoginRequiredMixin, UpdateView):
    model = Patient
    fields = ['name','identity_card_number','address','description','transfer','patient_number','patient_status','time_registered']

class PatientDelete(LoginRequiredMixin, DeleteView):
    model = Patient
    success_url = reverse_lazy('patient_list') #where to redirect after deleted
