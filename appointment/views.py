from django.shortcuts import render

# Create your views here.
def appointmentindex(request):
    return render(request, 'appointmentindex.html')