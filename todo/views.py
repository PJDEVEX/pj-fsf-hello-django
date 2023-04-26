from django.shortcuts import render
from .models import Item


# Create your views here.
def get_todo_list(request):   # Query the database to retrieve all items 
    items = Item.objects.all()
    context = {
        'items': items  # Create a dictionary with 'items' key and value
                        # as items variable

    }
    return render(request, 'todo/todo_list.html', context) 
    # Render the template with context dictionary and
    # return the HttpResponse object
