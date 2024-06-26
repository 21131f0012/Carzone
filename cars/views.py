from django.shortcuts import render,get_object_or_404
from .models import Car
from django.core.paginator import EmptyPage,Paginator, PageNotAnInteger

# Create your views here.
def cars(request):
    cars=Car.objects.order_by('-created_date')
    paginator=Paginator(cars,2)
    page=request.GET.get('page')
    paged_cars=paginator.get_page(page)
    model_search=Car.objects.values_list('model',flat=True).distinct()
    city_search=Car.objects.values_list('city',flat=True).distinct()
    year_search=Car.objects.values_list('year',flat=True).distinct()
    body_style_search=Car.objects.values_list('body_style',flat=True).distinct()
    data={
        'cars':paged_cars,
        'model_search':model_search,
        'city_search':city_search,
        'year_search':year_search,
        'body_style_search':body_style_search,
    }
    return render(request,'cars/cars.html',data)

def car_details(request,id):
    single_car=get_object_or_404(Car,pk=id)
    data={
        'single_car':single_car,
    }
    return render(request,'cars/cardetails.html',data)

def search(request):
    cars=Car.objects.order_by('-created_date')

    model_search=Car.objects.values_list('model',flat=True).distinct()
    city_search=Car.objects.values_list('city',flat=True).distinct()
    year_search=Car.objects.values_list('year',flat=True).distinct()
    body_style_search=Car.objects.values_list('body_style',flat=True).distinct()
    transmission_search=Car.objects.values_list('transmission',flat=True).distinct()
    if 'keyword' in request.GET:
        keyword=request.GET['keyword']
        if keyword:
            cars=Car.objects.filter(car_title__icontains=keyword)

    if 'model' in request.GET:
        model=request.GET['model']
        if model:
            cars=cars.filter(model__iexact=model)
    if 'city' in request.GET:
        city=request.GET['city']
        if city:
            cars=cars.filter(city__iexact=city)
    if 'year' in request.GET:
        year=request.GET['year']
        if year:
            cars=cars.filter(year__iexact=year)
    if  'body_style' in request.GET:
        body_style=request.GET['body_style']
        if  body_style:
            cars=cars.filter(body_style__iexact=body_style)
    if 'transmission' in request.GET:
        transmission=request.GET['transmission']
        if transmission:
            cars=cars.filter(transmission__exact=transmission)
    data={
        'cars':cars,
        'model_search':model_search,
        'city_search':city_search,
        'year_search':year_search,
        'body_style_search':body_style_search,
        'transmission_search':transmission_search,
    }
    return render(request,'cars/search.html',data)