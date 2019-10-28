from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect

# Create your views here.
def staffindex(request):
    return render(request, 'staffindex.html')

def staffregister(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            return redirect('staffindex')
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

    form = UserCreationForm
    return render(request = request,
                template_name = "staffinfo/staffregister.html",
                context={"form":form})