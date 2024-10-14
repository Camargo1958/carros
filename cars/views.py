from django.shortcuts import render, redirect
#from django.http import HttpResponse
from cars.models import Car
from cars.forms import CarModelForm
from django.views import View

# Create your views here.

class CarsView(View):
    def get(self, request):
        cars = Car.objects.all().order_by('model')
        search = request.GET.get('search')

        if search:
            cars = cars.filter(model__icontains=search) # contains (pesquisa por modelo ignore case)

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
