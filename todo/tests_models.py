from django.test import TestCase
from .models import Item


class TestModels (TestCase):

    def test_done_defaults_to_defaults(self):
        """
        Test that a todo item is created with a default done status of False
        """
        # Creating a new item      
        item = Item.objects.create(name='Test Todo Item')
        # Asserting that the done status of the item is False
        self.assertFalse(item.done)
