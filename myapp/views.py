from django.shortcuts import render, redirect
from .forms import IncidentForm
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.
def index(request): 
    form = IncidentForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request,"Registered Successfully !")
        return HttpResponseRedirect('/')
    context = {
        "form": form
    }

    return render(request, 'index.html',context)