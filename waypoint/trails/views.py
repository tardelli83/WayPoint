from django.shortcuts import render
from .models import Trail


def trail_list(request):
    trails = Trail.objects.filter(is_open=True).order_by('distance_km')
    return render(request, 'catalog.html', {'trails': trails})


from django.shortcuts import render

# Create your views here.
