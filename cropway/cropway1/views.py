from django.shortcuts import render
import re
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from cropway1.models import Crop  # Assuming your model is named Crop



def home(request):
    return render(request, 'home.html')
def choose_farm_path(request):
    return render(request, 'choose_farm_path.html')
def land_farming_view(request):
    return render(request, 'land_farming.html')  # create this template

def rooftop_farming_view(request):
    return render(request, 'rooftop_farming.html')  # create this template

@csrf_exempt
def recommend_crops(request):
    soil = request.GET.get('soilType')
    water = request.GET.get('waterAvailability')

    crops = Crop.objects.filter(soil_type=soil, water_availability=water)

    crop_data = []
    for crop in crops:
        crop_data.append({
            'name': crop.name,
            'yield': crop.expected_yield,
            'total_cost': crop.total_cost,
            'usage': crop.usage,
            'disadvantages': crop.disadvantages,
        })

    return JsonResponse({'crops': crop_data})