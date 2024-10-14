from django.shortcuts import render, redirect
#from django.http import HttpResponse
from cars.models import Car
from cars.forms import CarModelForm

# Create your views here.
def cars_view(request):
    cars = Car.objects.all().order_by('model')
    search = request.GET.get('search')

    if search:
        cars = cars.filter(model__icontains=search) # contains (pesquisa por modelo ignore case)
        
    #cars = Car.objects.filter(brand__name='Fiat')
    #cars = Car.objects.filter(model='Chevette Tubarão') # exact match
    #cars = Car.objects.filter(model__contains='Chevette') # contains

    return render(
        request, 
        'cars.html', 
        {'cars': cars}
    )

def new_car_view(request):
    if request.method == 'POST':
        new_car_form = CarModelForm(request.POST, request.FILES)
        #print(new_car_form.data)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')
    else:
        new_car_form = CarModelForm()
    return render(request, 'new_car.html', {'new_car_form': new_car_form})
