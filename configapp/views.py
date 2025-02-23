from django.shortcuts import render
from .models import *

def index(request):
    cars = Cars.objects.all()
    carmodel = Carmodel.objects.all()

    context ={
        "carmodel": carmodel,
        "cars":cars,
        "title":"News Title",
    }
    return render(request,'test.html', context=context)

def carmodel_new(request, carmodel_id):
    cars = Cars.objects.filter(carmodel_id=carmodel_id)
    carmodel = Carmodel.objects.all()

    context ={
        "carmodel": carmodel,
        "cars":cars,
        "title":"Cars Title",
    }
    return render(request,'index.html', context=context)

def batch_all(request, car_id):
    car = Cars.objects.get(pk=car_id)
    context ={
        "car": car
    }
    return render(request,'batch_all.html', context=context)

def carmodels(request):
    carmodels = Carmodel.objects.all()

    context = {
        "carmodels": carmodels,
    }
    return render(request,'carmodels.html', context=context)