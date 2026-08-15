from django.shortcuts import render

def home(request):
    """Render the homepage view."""
    return render(request, 'home.html')

def catalog(request):
    """Render the trail catalog view with 6 trail dicts."""
    trails = [
        {'name': 'Greenway Trail', 'distance': 5.23, 'elevation': 120.0, 'difficulty': 'easy', 'is_open': True},
        {'name': 'Ridgeback Loop', 'distance': 8.5, 'elevation': 340.5, 'difficulty': 'expert', 'is_open': True},
        {'name': 'Riverbank Path', 'distance': 3.12, 'elevation': 45.0, 'difficulty': 'easy', 'is_open': False},
        {'name': 'Pine Forest Way', 'distance': 6.4, 'elevation': 210.0, 'difficulty': 'medium', 'is_open': True},
        {'name': 'Canyon Ridge', 'distance': 11.0, 'elevation': 550.0, 'difficulty': 'expert', 'is_open': True},
        {'name': 'Meadow Walk', 'distance': 2.8, 'elevation': 30.0, 'difficulty': 'easy', 'is_open': True},
    ]
    return render(request, 'catalog.html', {'trails': trails})

def search(request):
    """Render the search view."""
    return render(request, 'search.html')

<<<<<<< Updated upstream
        # Showing the thank you page with the reporter's name
        return render(request, 'thank_you.html', {'name': name})

    # If it is a GET request, show the empty form page
    return render(request, 'report.html')


def search_view(request):
    # Safely read the 'q' parameter from the GET request, defaulting to an empty string
    query = request.GET.get("q", "")

    # Render the search template and pass the query into the context
    return render(request, 'search.html', {'query': query})


def catalog_view(request):
    # List of at least 6 trail dictionaries matching domain model attributes & Django requirements
    trails = [
        {'name': 'Greenway Trail', 'distance': 5.2, 'elevation_gain': 120.5, 'difficulty': 'easy', 'is_open': True},
        {'name': 'Pine Ridge Loop', 'distance': 8.7, 'elevation_gain': 340.0, 'difficulty': 'moderate',
         'is_open': True},
        {'name': 'Summit Peak Climb', 'distance': 12.4, 'elevation_gain': 850.2, 'difficulty': 'hard',
         'is_open': False},
        {'name': 'River Bank Path', 'distance': 3.1, 'elevation_gain': 45.0, 'difficulty': 'easy', 'is_open': True},
        {'name': 'Canyon Ridge', 'distance': 10.0, 'elevation_gain': 520.8, 'difficulty': 'hard', 'is_open': True},
        {'name': 'Valley Woods Way', 'distance': 6.5, 'elevation_gain': 210.0, 'difficulty': 'moderate',
         'is_open': False},
    ]

    context = {'trails': trails}
    return render(request, 'catalog.html', context)
=======
def report(request):
    """Render the report view."""
    return render(request, 'report.html')
>>>>>>> Stashed changes
