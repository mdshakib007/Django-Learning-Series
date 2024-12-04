from django.shortcuts import render
from brand.models import BrandModel


# Create your views here.
def brand_profile_view(request, id):
    brand_name = BrandModel.objects.get(pk=id)
    return render(request, 'brand/brand_profile.html', {'brand' : brand_name})