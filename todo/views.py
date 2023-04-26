from django.shortcuts import render
from .models import Item


# Create your views here.
def get_todo_list(request):   # Query the database to retrieve all items 
    items = Item.objects.all()
    context = {
        'items': items  # Create a dictionary with 'items' key and value
                        # as items variable

    }
    # Render the template with context dictionary and
    # return the HttpResponse object
    return render(request, 'todo/todo_list.html', context)


def add_item(request):
    """
    Renders the 'add_item.html' template when the add_item view is requested.
    """
    return render(request, 'todo/add_item.html')
