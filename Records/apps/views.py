from django.shortcuts import render
from .models import Employee

def display(request):

    employees = Employee.objects.all()
    context = {'employees': employees}

    return render(request, 'apps/display.html', context=context)
