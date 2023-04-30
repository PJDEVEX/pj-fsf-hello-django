from django.test import TestCase
from .models import Item


class TestModels(TestCase):

    def test_done_defaults_to_defaults(self):
        """
        Test that a todo item is created with a default done status of False
        """
        # Creating a new item
        item = Item.objects.create(name='Test Todo Item')
        # Asserting that the done status of the item is False
        self.assertFalse(
            item.done,
            "Expected the default value of 'done' to be False."
        )

    def test_item_string_method_returns_name(self):
        """
        Check if the item's name is correctly returned as a string
        """
        # Create a new item with a name
        item = Item.objects.create(name='Test Todo Item')
        # Assert that the item's name is returned as expected
        self.assertEqual(str(item), 'Test Todo Item')
