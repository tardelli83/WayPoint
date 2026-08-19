from django.shortcuts import render, get_object_or_404
from .models import Trail, Park, TrailReport


def trail_list(request):
    trails = Trail.objects.filter(is_open=True).order_by('distance_km')
    return render(request, 'catalog.html', {'trails': trails})


def search_trails(request):
    # Get the search query from the GET parameters
    query = request.GET.get('q', '')

    # Print debug info to the PyCharm terminal to track what the server sees
    print(f"--- QUERY RECEIVED: '{query}' ---")
    print(f"--- ALL TRAILS SEEN BY THE SERVER: {list(Trail.objects.values_list('name', flat=True))} ---")

    trails = []
    if query:
        # Filter trails case-insensitively using the query string
        trails = Trail.objects.filter(name__icontains=query)
        print(f"--- RESULTS FOUND: {list(trails.values_list('name', flat=True))} ---")

    # Render the search template with the query and the filtered results
    return render(request, 'search.html', {'trails': trails, 'query': query})



def trails_by_park(request, park_id):
    # WP-705: Cross-relation query to filter trails for a specific park
    park = get_object_or_404(Park, pk=park_id)
    trails = Trail.objects.filter(park=park)

    context = {'park': park, 'trails': trails}
    return render(request, 'catalog.html', context)


def report_view(request):
    # Handle form submission via POST
    if request.method == 'POST':
        # Extract form data sent by the user
        name = request.POST.get('name')
        email = request.POST.get('email')
        trail = request.POST.get('trail')
        note = request.POST.get('note')

        # Save the report permanently into the database
        TrailReport.objects.create(
            name=name,
            email=email,
            trail=trail,
            note=note
        )

        # Render the thank-you page and pass the user's name to the context
        return render(request, 'thank_you.html', {'name': name})

    # If the request is GET, render the blank report form page
    return render(request, 'report_form.html')