from django.shortcuts import render

# Create your views here.
def staffindex(request):
    return render(request, 'staffindex.html')