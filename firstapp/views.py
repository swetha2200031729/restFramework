from django.http import JsonResponse
from django.shortcuts import render
from firstapp.models import *;

# Create your views here.
def employeeView(request):
    emp = {
        'id' : 1919,
        'name' : 'sushma',
        'salary' : 500000000
    }

    return JsonResponse(emp)
