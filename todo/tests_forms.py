from django.test import TestCase
from .forms import ItemForm


class TestItemForm (TestCase):

    def test_item_name_is_required(self):
        """
        Ensure that this thing works correctly.
        """
        form = ItemForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_done_field_are_explicit_in_form_mataclass(self):
        """
        Ensure that this thing works correctly.
        """
        form = ItemForm()
        self.assertEqual(form.Meta.fields, ['name', 'done'])
