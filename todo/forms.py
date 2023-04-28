from django import forms
from .models import Item


# form class called ItemForm which inherits from forms.ModelForm
class ItemForm(forms.ModelForm):
    # An inner class called Meta which provides metadata about the form
    class Meta:
        # The model which the form is associated with
        model = Item
        # The fields which should be displayed on the form
        fields = ['name', 'done']
