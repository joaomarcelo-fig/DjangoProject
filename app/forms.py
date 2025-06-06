from django import forms
from .models import Item, Publisher, Category, Author

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['name', 'description']
        
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'description']
