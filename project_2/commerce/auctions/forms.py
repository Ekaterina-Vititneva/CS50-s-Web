from django import forms
from .models import Listing

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'description', 'imageURL', 'category', 'bid']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'imageURL': forms.URLInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'bid': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class BidForm(forms.Form):
    bid = forms.DecimalField(label="Place Bid", widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0.00€'}))
    
class CommentForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add a comment...'}))