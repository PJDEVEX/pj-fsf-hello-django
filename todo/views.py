from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm


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
    If a POST request is made, it creates a new item with the given name
    and 'done' status and redirects to the 'get_todo_list' view.
    """
    if request.method == 'POST':  # Check if request method is POST
        form = ItemForm(request.POST) 
        if form.is_valid():
            form.save()
            # Redirect to 'get_todo_list' view
            return redirect('get_todo_list')
    form = ItemForm()  # Create an instance of the ItemForm
    context = {
        'form': form  # Add the ItemForm instance to the context dictionary
    }
    # Render 'add_item.html' template for GET requests
    return render(request, 'todo/add_item.html', context)
