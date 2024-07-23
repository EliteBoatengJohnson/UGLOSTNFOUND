from django import forms
from .models import Item, Claim

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['category', 'name', 'description', 'location','date_found' ,'status', 'image']

class ClaimForm(forms.ModelForm):
    class Meta:
        model = Claim
        fields = ['description']




