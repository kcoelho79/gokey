# -*- encoding: utf-8 -*-
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import Resident
from api.models import Events

#@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('index.html')
    return HttpResponse(html_template.render(context, request))

#@login_required(login_url="/login/")
class ResidentCreate(CreateView):
    model = Resident
    fields = ['name', 'serial']

class ResidentList(ListView):
    model = Resident

def EventList(request):
    eventos = Events.objects.all()
    return render(request, 'api/events_list.html' , {'object_list':eventos})

def EventDelete(request, id):
    event = Events.objects.get(id=id)
    event.delete()
    return redirect('EventList')

def EventDeleteAll(request):
    event = Events.objects.all()
    event.delete()
    return redirect('EventList')

def ResidentImport(request):
    if request.method == 'POST':
        host = request.POST.get('host', None)
        print("HOST:",host)
        #conectar
        #importar
        #comparar lista
        #adicionar
        return redirect('ListResident')
    else:
        return render(request, 'app/resident_import.html')

def ResidentDelete(request, id):
    resident = Resident.objects.get(id=id)
    resident.delete()
    return redirect('ListResident')

#@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template(load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('page-500.html')
        return HttpResponse(html_template.render(context, request))
