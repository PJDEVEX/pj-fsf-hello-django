from django.test import TestCase
from .models import Item


class TestViews (TestCase):

    def test_get_todo_list(self):
        """
        Test that the todo list page is accessible and
        returns a 200 OK status code
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        # Test that the correct template is being used
        # to render the todo list page
        self.assertTemplateUsed(response, 'todo/todo_list.html')

    def test_get_add_item_page(self):
        """
        Test that the add item page is accessible and
        returns a 200 OK status code
        """
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)
        # Test that the correct template is being used
        # to render the add item page
        self.assertTemplateUsed(response, 'todo/add_item.html')

    def test_get_edit_item_page(self):
        """
        Test that the edit item page is accessible and
        returns a 200 OK status code
        """
        item = Item.objects.create(name='Test Todo Item')
        response = self.client.get(f'/edit/{item.id}')
        self.assertEqual(response.status_code, 200)
        # Test that the correct template is being used
        # to render the edit item page
        self.assertTemplateUsed(response, 'todo/edit_item.html')

    def test_can_add_item(self):
        """
        Test that a new item can be added to the todo list
        """
        response = self.client.post('/add', {'name': 'Test add Item'})
        # Test that the view redirects back to the todo list page
        # after a new item is added
        self.assertRedirects(response, '/')

    def test_can_delete_item(self):
        """
        Create a new item to be deleted
        """
        item = Item.objects.create(name='Test Todo Item')
        # Test that the delete view can be accessed for the new item
        response = self.client.get(f'/delete/{item.id}')
        # Test that the view redirects back to the todo list page
        # after the item is deleted
        self.assertRedirects(response, '/')
        # Test that the item has been successfully deleted
        existing_items = Item.objects.filter(id=item.id)
        self.assertEqual(len(existing_items), 0)

    def test_can_toggle_item(self):
        """
        Create a new item to be toggle
        """
        item = Item.objects.create(name='Test Todo Item', done=True)
        # Test that the toggle view can be accessed for the new item
        response = self.client.get(f'/toggle/{item.id}')
        # Test that the view redirects back to the todo list page
        # after the item is toggled
        self.assertRedirects(response, '/')
        updated_item = Item.objects.get(id=item.id)
        self.assertFalse(updated_item.done)
