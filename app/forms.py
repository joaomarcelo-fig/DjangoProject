from django import forms
<<<<<<< HEAD
from .models import Item, Category

=======
from .models import Item, Publisher
>>>>>>> developer

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description']

<<<<<<< HEAD
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
=======
class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['name', 'description']

>>>>>>> developer
