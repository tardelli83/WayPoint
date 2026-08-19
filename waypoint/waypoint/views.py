from django.shortcuts import render
from trails.models import Trail


def home(request):
    """Render the homepage view."""
    return render(request, 'home.html')


def catalog(request):
    """Render the trail catalog view from the database."""
    trails = Trail.objects.filter(is_open=True).order_by('distance_km')
    context = {'trails': trails}
    return render(request, 'catalog.html', context)


def search(request):
    """Render the search view with optional query parameter."""
    query = request.GET.get("q", "")

    # Esegue la ricerca sul database usando i campi corretti
    trails = []
    if query:
        trails = Trail.objects.filter(name__icontains=query)

    return render(request, 'search.html', {'trails': trails, 'query': query})


def report(request):
    """Render the report view."""
    return render(request, 'report_form.html')