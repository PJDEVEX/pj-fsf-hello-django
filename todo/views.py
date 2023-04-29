from django.shortcuts import render, redirect, get_object_or_404
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


def edit_item(request, item_id):
    """
    Renders the 'edit_item.html' template to edit an item.
    :param request: The HTTP request object.
    :param item_id: The id of the item to be edited.
:   return: A render object with the edit_item.html template
    """
    # Get the item with the given id
    item = get_object_or_404(Item, id=item_id)
    # Check if request method is POST
    if request.method == 'POST': 
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            # Redirect to 'get_todo_list' view
            return redirect('get_todo_list')
    # If request method is not POST, create an instance of the ItemForm
    # with the retrieved item instance
    form = ItemForm(instance=item)
    context = {
        # Add the ItemForm instance to the context dictionary
        'form': form
    }
    # Render the 'edit_item.html' template with the context dictionary
    return render(request, 'todo/edit_item.html', context)


def toggle_item(request, item_id):
    """
    Toggles the 'done' status of the item with the given id.
    :param request: The HTTP request object.
    :param item_id: The id of the item to be toggled.
    :return: A redirect object to 'get_todo_list' view.
    """
    # Get the item with the given id
    item = get_object_or_404(Item, id=item_id)
    # Toggle the 'done' status of the item
    item.done = not item.done
    item.save()
    # Redirect to the 'get_todo_list' view
    return redirect('get_todo_list')


def delete_item(request, item_id):
    """
    Deletes the item with the given id.
    :param request: The HTTP request object.
    :param item_id: The id of the item to be deleted.
    :return: A redirect object to 'get_todo_list' view.
    """
    # Get the item with the given id
    item = get_object_or_404(Item, id=item_id)
    # Delete the item
    item.delete()
    # Redirect to the 'get_todo_list' view
    return redirect('get_todo_list')
