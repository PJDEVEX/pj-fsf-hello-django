from django.test import TestCase
from .forms import ItemForm


class TestItemForm (TestCase):

    def test_item_name_is_required(self):
        """
        Test that an error is raised if the item name field is left blank.
        """
        form = ItemForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_done_field_is_not_required(self):
        """
        Test that the 'done' field is not required.
        """
        form = ItemForm({'name': 'Test Todo Item'})
        self.assertTrue(form.is_valid())

    def test_field_are_explicit_in_form_mataclass(self):
        """
        Test that the fields 'name' and 'done' are explicitly defined
        in the form meta class.
        """
        form = ItemForm()
        self.assertEqual(form.Meta.fields, ['name', 'done'])
