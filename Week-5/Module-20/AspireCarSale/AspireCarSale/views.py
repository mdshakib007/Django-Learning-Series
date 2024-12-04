from django.shortcuts import render
from car.models import CarModel
from brand.models import BrandModel


def home(request, brand_slug = None):
    cars = CarModel.objects.all()
    brands = BrandModel.objects.all()
    curr_brand = None

    if brand_slug is not None:
        brand = BrandModel.objects.get(slug= brand_slug)
        curr_brand = brand.name
        cars = CarModel.objects.filter(brand=brand)
    return render(request, 'home.html', {'cars' : cars, 'brands' : brands, 'curr_brand' : curr_brand})

