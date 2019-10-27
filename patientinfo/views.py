from django.shortcuts import render
from django.views import generic
from django.db.models import Q #to query multiple filter
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView #easily create,update,view form
from django.urls import reverse_lazy
# importing Patient models
from patientinfo.models import Patient
# importing date time
# from datetime import datetime

@login_required
def patientinfohome(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    patient_number = Patient.objects.all().count()
    patient_act = Patient.objects.filter(patient_status__exact='Active').count()
    patient_rip = Patient.objects.filter(patient_status__exact='Rest In Peace').count()   
    patient_mia = Patient.objects.filter(patient_status__exact='Missing').count()

    #input query to display user input year graph
    query = request.GET.get('q')
    if not query:
            currentyear = 0000

            # for year 2015
            patient_year2015_mia = Patient.objects.filter(Q(time_registered__year=2015)&Q(patient_status__contains="Missing")).count()
            patient_year2015_act = Patient.objects.filter(Q(time_registered__year=2015)&Q(patient_status__contains="Active")).count()
            patient_year2015_rip = Patient.objects.filter(Q(time_registered__year=2015)&Q(patient_status__contains="Rest In Peace")).count()
            
            # for year 2016
            patient_year2016_mia = Patient.objects.filter(Q(time_registered__year=2016)&Q(patient_status__contains="Missing")).count()
            patient_year2016_act = Patient.objects.filter(Q(time_registered__year=2016)&Q(patient_status__contains="Active")).count()
            patient_year2016_rip = Patient.objects.filter(Q(time_registered__year=2016)&Q(patient_status__contains="Rest In Peace")).count()

            # for year 2017
            patient_year2017_mia = Patient.objects.filter(Q(time_registered__year=2017)&Q(patient_status__contains="Missing")).count()
            patient_year2017_act = Patient.objects.filter(Q(time_registered__year=2017)&Q(patient_status__contains="Active")).count()
            patient_year2017_rip = Patient.objects.filter(Q(time_registered__year=2017)&Q(patient_status__contains="Rest In Peace")).count()

            # for year 2018
            patient_year2018_mia = Patient.objects.filter(Q(time_registered__year=2018)&Q(patient_status__contains="Missing")).count()
            patient_year2018_act = Patient.objects.filter(Q(time_registered__year=2018)&Q(patient_status__contains="Active")).count()
            patient_year2018_rip = Patient.objects.filter(Q(time_registered__year=2018)&Q(patient_status__contains="Rest In Peace")).count()

            # for year 2019
            patient_year2019_mia = Patient.objects.filter(Q(time_registered__year=2019)&Q(patient_status__contains="Missing")).count()
            patient_year2019_act = Patient.objects.filter(Q(time_registered__year=2019)&Q(patient_status__contains="Active")).count()
            patient_year2019_rip = Patient.objects.filter(Q(time_registered__year=2019)&Q(patient_status__contains="Rest In Peace")).count()

            context = {
            'patient_number': patient_number,
            'patient_total_act': patient_act,
            'patient_total_rip': patient_rip,
            'patient_total_mia': patient_mia,

            'patient_year2015_mia': patient_year2015_mia,
            'patient_year2015_act': patient_year2015_act,
            'patient_year2015_rip': patient_year2015_rip,    
            'patient_year2016_mia': patient_year2016_mia,
            'patient_year2016_act': patient_year2016_act,
            'patient_year2016_rip': patient_year2016_rip,
            'patient_year2017_mia': patient_year2017_mia,
            'patient_year2017_act': patient_year2017_act,
            'patient_year2017_rip': patient_year2017_rip,
            'patient_year2018_mia': patient_year2018_mia,
            'patient_year2018_act': patient_year2018_act,
            'patient_year2018_rip': patient_year2018_rip,
            'patient_year2019_mia': patient_year2019_mia,
            'patient_year2019_act': patient_year2019_act,
            'patient_year2019_rip': patient_year2019_rip,
            'currentyear': currentyear,
            }
    else:
            patient_total_year = Patient.objects.filter(time_registered__year=query).count()
            # display current patient for each of the status
            patient_yearinput_mia = Patient.objects.filter(Q(time_registered__year=query)&Q(patient_status__contains="Missing")).count()
            patient_yearinput_act = Patient.objects.filter(Q(time_registered__year=query)&Q(patient_status__contains="Active")).count()
            patient_yearinput_rip = Patient.objects.filter(Q(time_registered__year=query)&Q(patient_status__contains="Rest In Peace")).count()
            currentyear = query

            #query to get number of patient for each status, each month in selected year from input
            patient_year_mia_01 = Patient.objects.filter(Q(time_registered__year=currentyear)&Q(time_registered__month=1)&Q(patient_status__contains="Missing")).count()
            patient_year_mia_02 = Patient.objects.filter(Q(time_registered__year=currentyear)&Q(time_registered__month=2)&Q(patient_status__contains="Missing")).count()
            patient_year_mia_03 = Patient.objects.filter(Q(time_registered__year=currentyear)&Q(time_registered__month=3)&Q(patient_status__contains="Missing")).count()
            patient_year_mia_04 = Patient.objects.filter(Q(time_registered__year=currentyear)&Q(time_registered__month=4)&Q(patient_status__contains="Missing")).count()
            patient_year_mia_05 = Patient.objects.filter(Q(time_registered__year=currentyear)&Q(time_registered__month=5)&Q(patient_status__contains="Missing")).count()
            patient_year_mia_06 = Patient.objects.filter(Q(time_registered__year=currentyear)&Q(time_registered__month=6)&Q(patient_status__contains="Missing")).count()
            patient_year_mia_07 = Patient.objects.filter(Q(time_registered__year=currentyear)&Q(time_registered__month=7)&Q(patient_status__contains="Missing")).count()
            patient_year_mia_08 = Patient.objects.filter(Q(time_registered__year=currentyear)&Q(time_registered__month=8)&Q(patient_status__contains="Missing")).count()
            patient_year_mia_09 = Patient.objects.filter(Q(time_registered__year=currentyear)&Q(time_registered__month=9)&Q(patient_status__contains="Missing")).count()
            patient_year_mia_10 = Patient.objects.filter(Q(time_registered__year=currentyear)&Q(time_registered__month=10)&Q(patient_status__contains="Missing")).count()
            patient_year_mia_11 = Patient.objects.filter(Q(time_registered__year=currentyear)&Q(time_registered__month=11)&Q(patient_status__contains="Missing")).count()
            patient_year_mia_12 = Patient.objects.filter(Q(time_registered__year=currentyear)&Q(time_registered__month=12)&Q(patient_status__contains="Missing")).count()
            patient_year_act_01 = Patient.objects.filter(Q(time_registered__year=currentyear)&Q(time_registered__month=1)&Q(patient_status__contains="Active")).count()
            patient_year_act_02 = Patient.objects.filter(Q(time_registered__year=currentyear)&Q(time_registered__month=2)&Q(patient_status__contains="Active")).count()
            patient_year_act_03 = Patient.objects.filter(Q(time_registered__year=currentyear)&Q(time_registered__month=3)&Q(patient_status__contains="Active")).count()
            patient_year_act_04 = Patient.objects.filter(Q(time_registered__year=currentyear)&Q(time_registered__month=4)&Q(patient_status__contains="Active")).count()
            patient_year_act_05 = Patient.objects.filter(Q(time_registered__year=currentyear)&Q(time_registered__month=5)&Q(patient_status__contains="Active")).count()
            patient_year_act_06 = Patient.objects.filter(Q(time_registered__year=currentyear)&Q(time_registered__month=6)&Q(patient_status__contains="Active")).count()
            patient_year_act_07 = Patient.objects.filter(Q(time_registered__year=currentyear)&Q(time_registered__month=7)&Q(patient_status__contains="Active")).count()
            patient_year_act_08 = Patient.objects.filter(Q(time_registered__year=currentyear)&Q(time_registered__month=8)&Q(patient_status__contains="Active")).count()
            patient_year_act_09 = Patient.objects.filter(Q(time_registered__year=currentyear)&Q(time_registered__month=9)&Q(patient_status__contains="Active")).count()
            patient_year_act_10 = Patient.objects.filter(Q(time_registered__year=currentyear)&Q(time_registered__month=10)&Q(patient_status__contains="Active")).count()
            patient_year_act_11 = Patient.objects.filter(Q(time_registered__year=currentyear)&Q(time_registered__month=11)&Q(patient_status__contains="Active")).count()
            patient_year_act_12 = Patient.objects.filter(Q(time_registered__year=currentyear)&Q(time_registered__month=12)&Q(patient_status__contains="Active")).count()
            patient_year_rip_01 = Patient.objects.filter(Q(time_registered__year=currentyear)&Q(time_registered__month=1)&Q(patient_status__contains="Rest In Peace")).count()
            patient_year_rip_02 = Patient.objects.filter(Q(time_registered__year=currentyear)&Q(time_registered__month=2)&Q(patient_status__contains="Rest In Peace")).count()
            patient_year_rip_03 = Patient.objects.filter(Q(time_registered__year=currentyear)&Q(time_registered__month=3)&Q(patient_status__contains="Rest In Peace")).count()
            patient_year_rip_04 = Patient.objects.filter(Q(time_registered__year=currentyear)&Q(time_registered__month=4)&Q(patient_status__contains="Rest In Peace")).count()
            patient_year_rip_05 = Patient.objects.filter(Q(time_registered__year=currentyear)&Q(time_registered__month=5)&Q(patient_status__contains="Rest In Peace")).count()
            patient_year_rip_06 = Patient.objects.filter(Q(time_registered__year=currentyear)&Q(time_registered__month=6)&Q(patient_status__contains="Rest In Peace")).count()
            patient_year_rip_07 = Patient.objects.filter(Q(time_registered__year=currentyear)&Q(time_registered__month=7)&Q(patient_status__contains="Rest In Peace")).count()
            patient_year_rip_08 = Patient.objects.filter(Q(time_registered__year=currentyear)&Q(time_registered__month=8)&Q(patient_status__contains="Rest In Peace")).count()
            patient_year_rip_09 = Patient.objects.filter(Q(time_registered__year=currentyear)&Q(time_registered__month=9)&Q(patient_status__contains="Rest In Peace")).count()
            patient_year_rip_10 = Patient.objects.filter(Q(time_registered__year=currentyear)&Q(time_registered__month=10)&Q(patient_status__contains="Rest In Peace")).count()
            patient_year_rip_11 = Patient.objects.filter(Q(time_registered__year=currentyear)&Q(time_registered__month=11)&Q(patient_status__contains="Rest In Peace")).count()
            patient_year_rip_12 = Patient.objects.filter(Q(time_registered__year=currentyear)&Q(time_registered__month=12)&Q(patient_status__contains="Rest In Peace")).count()

            context = { 
            'patient_number': patient_number,
            'patient_total_act': patient_act,
            'patient_total_rip': patient_rip,
            'patient_total_mia': patient_mia,
            'patient_total_year': patient_total_year,
            'patient_yearinput_mia': patient_yearinput_mia,
            'patient_yearinput_act': patient_yearinput_act,
            'patient_yearinput_rip': patient_yearinput_rip,
            'currentyear': currentyear,
            'patient_year_mia_01': patient_year_mia_01,
            'patient_year_mia_02': patient_year_mia_02,
            'patient_year_mia_03': patient_year_mia_03,
            'patient_year_mia_04': patient_year_mia_04,
            'patient_year_mia_05': patient_year_mia_05,
            'patient_year_mia_06': patient_year_mia_06,
            'patient_year_mia_07': patient_year_mia_07,
            'patient_year_mia_08': patient_year_mia_08,
            'patient_year_mia_09': patient_year_mia_09,
            'patient_year_mia_10': patient_year_mia_10,
            'patient_year_mia_11': patient_year_mia_11,
            'patient_year_mia_12': patient_year_mia_12,
            'patient_year_act_01': patient_year_act_01,
            'patient_year_act_02': patient_year_act_02,
            'patient_year_act_03': patient_year_act_03,
            'patient_year_act_04': patient_year_act_04,
            'patient_year_act_05': patient_year_act_05,
            'patient_year_act_06': patient_year_act_06,
            'patient_year_act_07': patient_year_act_07,
            'patient_year_act_08': patient_year_act_08,
            'patient_year_act_09': patient_year_act_09,
            'patient_year_act_10': patient_year_act_10,
            'patient_year_act_11': patient_year_act_11,
            'patient_year_act_12': patient_year_act_12,
            'patient_year_rip_01': patient_year_rip_01,
            'patient_year_rip_02': patient_year_rip_02,
            'patient_year_rip_03': patient_year_rip_03,
            'patient_year_rip_04': patient_year_rip_04,
            'patient_year_rip_05': patient_year_rip_05,
            'patient_year_rip_06': patient_year_rip_06,
            'patient_year_rip_07': patient_year_rip_07,
            'patient_year_rip_08': patient_year_rip_08,
            'patient_year_rip_09': patient_year_rip_09,
            'patient_year_rip_10': patient_year_rip_10,
            'patient_year_rip_11': patient_year_rip_11,
            'patient_year_rip_12': patient_year_rip_12,

            }
    # patient_time_registered = Patient.objects.filter(time_registered=patient_year)

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'patientinfohome.html', context=context)
    
class PatientListView(LoginRequiredMixin, generic.ListView):
        model = Patient
        # paginate_by = 10
        # search function
        def get_queryset(self):
            query = self.request.GET.get('q')
            if query: #if search something
                object_list = self.model.objects.filter(Q(name__contains=query) | Q(identity_card_number__contains=query) | Q(transfer__contains=query) | Q(patient_status__contains=query))
                return object_list
            else: #no search, display all patient
                object_list = self.model.objects.all()
                return object_list

class PatientDetailView(LoginRequiredMixin, generic.DetailView):
    model = Patient

class PatientCreate(LoginRequiredMixin, CreateView):
    model = Patient
    # fields = ['name','identity_card_number','address','description','transfer','patient_number','patient_status','time_registered']
    fields = ['name','identity_card_number','transfer','patient_status','time_registered']
    success_url = reverse_lazy('patient_list') #where to redirect after create

class PatientUpdate(LoginRequiredMixin, UpdateView):
    model = Patient
    fields = ['name','identity_card_number','transfer','patient_status','time_registered']

class PatientDelete(LoginRequiredMixin, DeleteView):
    model = Patient
    success_url = reverse_lazy('patient_list') #where to redirect after deleted
