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

    # If the user simply opens the page -> GET method, show empty form
    return render(request, 'report.html')


def search_view(request):
    # Safely read the 'q' parameter from the GET request, defaulting to an empty string
    query = request.GET.get("q", "")

    # Render the search template and pass the query into the context
    return render(request, 'search.html', {'query': query})
