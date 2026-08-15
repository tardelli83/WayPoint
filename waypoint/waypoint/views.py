from django.shortcuts import render

def home_view(request):
    # Welcoming Message
    context = {'message': "Welcome to Waypoint, your trail website!"}
    return render(request, 'home.html', context)


def report_view(request):
    # If the user sent the form (clicking Submit) -> POST method
    if request.method == 'POST':
        # Reading the data sent through the form
        name = request.POST.get('name', 'Ospite')
        email = request.POST.get('email')
        trail = request.POST.get('trail')
        note = request.POST.get('note')

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