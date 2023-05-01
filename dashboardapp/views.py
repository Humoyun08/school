from django.shortcuts import render,redirect
from .models import*
from .forms import *
# Create your views here.
def index(request):
    return render(request,'dashboardapp/index.html')

def base(request):
    return render(request,'dashboardapp/base.html')

def mentorTable(request):
    mentors = Mentor.objects.all()
    context = {
        'mentors' : mentors
    }
    return render(request,'dashboardapp/m-table.html',context)

def mentorCreate(request):
    form = CreateMentorForms()
    if request.method == "POST":
        form = CreateMentorForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('m_table')
        else:
            form = CreateMentorForms()
            
    context = {
        'form' : form
    }
    return render(request,'dashboardapp/m-create.html',context)

def a1_class(request):
    pupils = A1_class.objects.all()
    context = {
        'pupils' : pupils
    }
    return render(request,'dashboardapp/1a-class.html',context)


def error(request):
    return render(request,'dashboardapp/error.html')


