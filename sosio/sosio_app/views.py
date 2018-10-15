from django.shortcuts import render
from django.http import HttpResponse
from .models import expenses


# Create your views here.
expenses = [
    {
        'Name':'John',
        'monthly_income':100000 ,
        'monthly_expenses_on_shelter':5000,
        'monthly_expenses_on_food':15000,
        'monthly_expenses_on_travel':5000,
        'other_expenses':10000,
    },
    {
        'Name':'Cary',
        'monthly_income':70000,
        'monthly_expenses_on_shelter':5000,
        'monthly_expenses_on_food':15000,
        'monthly_expenses_on_travel':3000,
        'other_expenses':5000,
    }
]

def index(request):
    context = {
    'expenses':expenses
    }
    return render(request,'sosio_app/index.html',context)

def info(request):
    return render(request, 'sosio_app/info.html',)
