from django.shortcuts import render

def home(request):
    """Render the homepage view."""
    return render(request, 'home.html')

from trails.models import Trail

def catalog(request):
    """Render the trail catalog view from the database."""
    trails = Trail.objects.filter(is_open=True).order_by('distance_km')
    context = {'trails': trails}
    return render(request, 'catalog.html', context)

def search(request):
    """Render the search view with optional query parameter."""
    query = request.GET.get("q", "")
    return render(request, 'search.html', {'query': query})

def report(request):
    """Render the report view."""
    return render(request, 'report.html')